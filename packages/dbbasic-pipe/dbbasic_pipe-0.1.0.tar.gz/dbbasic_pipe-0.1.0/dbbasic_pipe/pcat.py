#!/usr/bin/env python3
"""
Smart cat - reads files and respects backpressure signals.

Usage:
    pcat <file>

Works standalone or with PIPE_CONTROL_SOCKET coordination.

Examples:
    pcat data.json
    pcat data.json | pfilter 'age > 18'
"""

import os
import sys
import json
import socket
import select


def main():
    if len(sys.argv) < 2:
        print("Usage: pcat <file>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Error: file not found: {filename}", file=sys.stderr)
        sys.exit(1)

    # Check for coordination socket
    ctrl_socket = os.getenv('PIPE_CONTROL_SOCKET')
    sock = None
    limit = -1  # -1 = unlimited

    if ctrl_socket and os.path.exists(ctrl_socket):
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ctrl_socket)
            sock.setblocking(False)

            # Register
            msg = {
                'type': 'register',
                'pid': os.getpid(),
                'command': 'pcat',
                'file': filename
            }
            sock.send(json.dumps(msg).encode() + b'\n')

            print(f"[pcat] Registered, reading: {filename}", file=sys.stderr)

            # Wait a moment for backpressure signals
            import time
            time.sleep(0.1)

            # Check for backpressure
            readable, _, _ = select.select([sock], [], [], 0)
            if readable:
                try:
                    data = sock.recv(4096).decode()
                    for msg_line in data.strip().split('\n'):
                        if msg_line:
                            msg = json.loads(msg_line)
                            if msg['type'] == 'backpressure':
                                limit = msg['count']
                                print(f"[pcat] Received backpressure: {limit}", file=sys.stderr)
                except:
                    pass

        except Exception as e:
            print(f"[pcat] Coordination failed: {e}", file=sys.stderr)
            sock = None

    # Read and output file
    count = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Check for more control messages
                if sock:
                    readable, _, _ = select.select([sock], [], [], 0)
                    if readable:
                        try:
                            data = sock.recv(4096).decode()
                            for msg_line in data.strip().split('\n'):
                                if msg_line:
                                    msg = json.loads(msg_line)
                                    if msg['type'] == 'backpressure':
                                        if limit == -1:  # First time
                                            limit = msg['count']
                                            print(f"[pcat] Received backpressure: {limit}", file=sys.stderr)
                        except:
                            pass

                print(line, end='')
                sys.stdout.flush()
                count += 1

                # Stop if we hit the limit
                if limit > 0 and count >= limit * 2:  # 2x buffer for filtering
                    print(f"[pcat] Reached soft limit, stopping at {count} lines", file=sys.stderr)
                    break

    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        if sock:
            try:
                msg = {
                    'type': 'complete',
                    'pid': os.getpid(),
                    'lines_read': count
                }
                sock.send(json.dumps(msg).encode() + b'\n')
                sock.close()
            except:
                pass

        print(f"[pcat] Read {count} lines", file=sys.stderr)


if __name__ == '__main__':
    main()
