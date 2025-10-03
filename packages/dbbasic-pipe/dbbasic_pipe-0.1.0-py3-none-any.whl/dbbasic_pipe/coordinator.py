#!/usr/bin/env python3
"""
Pipe coordinator - routes control messages between pipeline commands.

Usage:
    pipe-coordinator <socket-path>

Example:
    pipe-coordinator /tmp/pipe-ctrl-1234.sock
"""

import socket
import os
import sys
import json
import select


def main():
    if len(sys.argv) < 2:
        print("Usage: pipe-coordinator <socket-path>", file=sys.stderr)
        sys.exit(1)

    sock_path = sys.argv[1]

    # Remove old socket if exists
    try:
        os.unlink(sock_path)
    except FileNotFoundError:
        pass

    # Create Unix domain socket
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(sock_path)
    server.listen(10)
    server.setblocking(False)

    clients = {}  # pid -> socket
    commands = {}  # pid -> command_info

    print(f"[coordinator] Listening on {sock_path}", file=sys.stderr)

    sockets = [server]

    try:
        while True:
            readable, _, _ = select.select(sockets, [], [], 1.0)

            for s in readable:
                if s is server:
                    # New connection
                    client, _ = server.accept()
                    client.setblocking(False)
                    sockets.append(client)
                else:
                    # Data from client
                    try:
                        data = s.recv(4096).decode()
                        if not data:
                            # Connection closed
                            sockets.remove(s)
                            # Remove from clients
                            for pid, sock in list(clients.items()):
                                if sock == s:
                                    del clients[pid]
                                    if pid in commands:
                                        del commands[pid]
                            s.close()
                            continue

                        for line in data.strip().split('\n'):
                            if line:
                                msg = json.loads(line)
                                handle_message(msg, s, clients, commands)

                    except json.JSONDecodeError as e:
                        print(f"[coordinator] JSON error: {e}", file=sys.stderr)
                    except Exception as e:
                        print(f"[coordinator] Error: {e}", file=sys.stderr)
                        sockets.remove(s)
                        s.close()

    except KeyboardInterrupt:
        print("\n[coordinator] Shutting down", file=sys.stderr)
    finally:
        server.close()
        try:
            os.unlink(sock_path)
        except:
            pass


def handle_message(msg, sender, clients, commands):
    """Route messages between pipeline commands."""
    msg_type = msg.get('type')

    if msg_type == 'register':
        pid = msg['pid']
        clients[pid] = sender
        commands[pid] = msg
        print(f"[coordinator] Registered {msg.get('command', 'unknown')} (pid {pid})", file=sys.stderr)

    elif msg_type == 'backpressure':
        # Broadcast to all OTHER clients (upstream)
        count = msg.get('count', 0)
        print(f"[coordinator] Broadcasting backpressure: {count}", file=sys.stderr)
        for pid, sock in clients.items():
            if sock != sender:
                try:
                    sock.send(json.dumps(msg).encode() + b'\n')
                except:
                    pass

    elif msg_type == 'complete':
        print(f"[coordinator] Command {msg.get('pid')} completed", file=sys.stderr)

    elif msg_type == 'error':
        print(f"[coordinator] Error from {msg.get('pid')}: {msg.get('message')}", file=sys.stderr)


if __name__ == '__main__':
    main()
