#!/usr/bin/env python3
"""
Limit command - outputs first N lines and signals backpressure.

Usage:
    plimit <count>

Works standalone or with PIPE_CONTROL_SOCKET coordination.

Examples:
    cat file.txt | plimit 10
    echo "test" | plimit 5
"""

import os
import sys
import socket
import json


def main():
    if len(sys.argv) < 2:
        print("Usage: plimit <count>", file=sys.stderr)
        sys.exit(1)

    try:
        limit = int(sys.argv[1])
    except ValueError:
        print(f"Error: count must be an integer", file=sys.stderr)
        sys.exit(1)

    # Check for coordination socket
    ctrl_socket = os.getenv('PIPE_CONTROL_SOCKET')
    sock = None

    if ctrl_socket and os.path.exists(ctrl_socket):
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ctrl_socket)

            # Register
            msg = {
                'type': 'register',
                'pid': os.getpid(),
                'command': 'plimit',
                'value': limit
            }
            sock.send(json.dumps(msg).encode() + b'\n')

            # Send backpressure signal
            msg = {
                'type': 'backpressure',
                'count': limit
            }
            sock.send(json.dumps(msg).encode() + b'\n')

            print(f"[plimit] Signaled backpressure: {limit}", file=sys.stderr)

        except Exception as e:
            print(f"[plimit] Coordination failed: {e}", file=sys.stderr)
            sock = None

    # Process data
    count = 0
    try:
        for line in sys.stdin:
            print(line, end='')
            count += 1
            if count >= limit:
                break
    except BrokenPipeError:
        # Downstream closed - expected
        pass
    except KeyboardInterrupt:
        pass
    finally:
        if sock:
            # Notify completion
            try:
                msg = {
                    'type': 'complete',
                    'pid': os.getpid(),
                    'processed': count
                }
                sock.send(json.dumps(msg).encode() + b'\n')
                sock.close()
            except:
                pass


if __name__ == '__main__':
    main()
