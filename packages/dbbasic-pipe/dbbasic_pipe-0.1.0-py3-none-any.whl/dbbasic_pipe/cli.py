#!/usr/bin/env python3
"""
Main CLI entry point for dbbasic-pipe.

This is the smart-pipe wrapper that enables coordination.
"""

import os
import sys
import subprocess
import signal
import time


def main():
    """Main entry point for dbbasic-pipe command."""
    if len(sys.argv) < 2:
        print("Usage: dbbasic-pipe <command>", file=sys.stderr)
        print("", file=sys.stderr)
        print("Example:", file=sys.stderr)
        print('  dbbasic-pipe bash -c "pcat data.json | pfilter \'age > 18\' | plimit 10"', file=sys.stderr)
        sys.exit(1)

    # Find coordinator in same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    coordinator_path = os.path.join(script_dir, "coordinator.py")

    # Create unique socket path
    pid = os.getpid()
    ctrl_sock = f"/tmp/pipe-ctrl-{pid}.sock"

    # Set environment variables for child processes
    env = os.environ.copy()
    env["PIPE_CONTROL_SOCKET"] = ctrl_sock
    env["PIPE_SESSION_ID"] = str(pid)

    # Start coordinator
    coordinator_proc = subprocess.Popen(
        [sys.executable, coordinator_path, ctrl_sock],
        env=env,
        stderr=subprocess.PIPE
    )

    # Wait for socket to be ready
    for _ in range(50):
        if os.path.exists(ctrl_sock):
            break
        time.sleep(0.01)
    else:
        print(f"[dbbasic-pipe] Error: Failed to start coordinator", file=sys.stderr)
        coordinator_proc.terminate()
        sys.exit(1)

    print(f"[dbbasic-pipe] Coordinator ready (PID: {coordinator_proc.pid})", file=sys.stderr)

    # Setup cleanup handler
    def cleanup(signum=None, frame=None):
        print(f"[dbbasic-pipe] Cleaning up...", file=sys.stderr)
        coordinator_proc.terminate()
        try:
            coordinator_proc.wait(timeout=1)
        except subprocess.TimeoutExpired:
            coordinator_proc.kill()
        try:
            os.unlink(ctrl_sock)
        except FileNotFoundError:
            pass

    # Register signal handlers
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    try:
        # Run the actual pipeline
        result = subprocess.run(sys.argv[1:], env=env)
        exit_code = result.returncode
    except KeyboardInterrupt:
        exit_code = 130
    except Exception as e:
        print(f"[dbbasic-pipe] Error: {e}", file=sys.stderr)
        exit_code = 1
    finally:
        cleanup()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
