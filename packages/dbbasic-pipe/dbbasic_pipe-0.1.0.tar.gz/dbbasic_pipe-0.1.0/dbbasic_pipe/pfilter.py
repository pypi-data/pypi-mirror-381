#!/usr/bin/env python3
"""
Filter command - filters JSON lines by simple expressions.

Usage:
    pfilter '<expression>'

Works standalone or with PIPE_CONTROL_SOCKET coordination.

Examples:
    cat data.json | pfilter 'age > 18'
    cat data.json | pfilter 'name == "Alice"'
    cat data.json | pfilter 'status == "active" and score > 50'
"""

import os
import sys
import json
import socket
import select


def main():
    if len(sys.argv) < 2:
        print("Usage: pfilter '<expression>'", file=sys.stderr)
        sys.exit(1)

    predicate = sys.argv[1]

    # Check for coordination socket
    ctrl_socket = os.getenv('PIPE_CONTROL_SOCKET')
    sock = None
    remaining = -1  # -1 = unlimited

    if ctrl_socket and os.path.exists(ctrl_socket):
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ctrl_socket)
            sock.setblocking(False)

            # Register
            msg = {
                'type': 'register',
                'pid': os.getpid(),
                'command': 'pfilter',
                'predicate': predicate
            }
            sock.send(json.dumps(msg).encode() + b'\n')

            print(f"[pfilter] Registered with predicate: {predicate}", file=sys.stderr)

        except Exception as e:
            print(f"[pfilter] Coordination failed: {e}", file=sys.stderr)
            sock = None

    # Process data
    processed = 0
    output = 0

    try:
        for line in sys.stdin:
            # Check for control messages
            if sock:
                readable, _, _ = select.select([sock], [], [], 0)
                if readable:
                    try:
                        data = sock.recv(4096).decode()
                        for msg_line in data.strip().split('\n'):
                            if msg_line:
                                msg = json.loads(msg_line)
                                if msg['type'] == 'backpressure':
                                    remaining = msg['count']
                                    print(f"[pfilter] Received backpressure: {remaining}", file=sys.stderr)
                    except:
                        pass

            processed += 1
            line = line.strip()
            if not line:
                continue

            # Parse and evaluate
            try:
                record = json.loads(line)
                if eval_predicate(record, predicate):
                    print(json.dumps(record))
                    sys.stdout.flush()
                    output += 1

                    if remaining > 0:
                        remaining -= 1
                        if remaining == 0:
                            print(f"[pfilter] Reached limit, stopping", file=sys.stderr)
                            break

            except json.JSONDecodeError:
                # Not JSON, try as plain text with simple eval
                try:
                    if eval(predicate, {"line": line, "text": line}):
                        print(line)
                        output += 1
                        if remaining > 0:
                            remaining -= 1
                            if remaining == 0:
                                break
                except:
                    # Can't evaluate, skip
                    pass

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
                    'processed': processed,
                    'output': output
                }
                sock.send(json.dumps(msg).encode() + b'\n')
                sock.close()
            except:
                pass

        print(f"[pfilter] Processed {processed}, output {output}", file=sys.stderr)


def eval_predicate(record, predicate):
    """Safely evaluate predicate against record."""
    try:
        # Create a safe namespace with record fields
        namespace = dict(record)
        # Also allow direct field access
        return eval(predicate, {"__builtins__": {}}, namespace)
    except:
        return False


if __name__ == '__main__':
    main()
