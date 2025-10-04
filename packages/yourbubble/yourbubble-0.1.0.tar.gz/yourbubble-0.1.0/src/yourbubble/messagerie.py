#!/usr/bin/env python3
"""
yourbubble.messagerie v1.0
Interactive CLI for ephemeral, encrypted UDP messaging.
Philosophy: "Send. Receive. Vanish."
"""

import argparse
import sys
import getpass
from .protocol import BubbleSender, BubbleListener

def main():
    parser = argparse.ArgumentParser(
        description="yourbubble — send and receive ephemeral bubbles",
        epilog="The bubble exists only while it is needed.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # === SEND ===
    send_parser = subparsers.add_parser("send", help="Send an ephemeral bubble")
    send_parser.add_argument("ip", help="Recipient IP address (e.g., 192.168.1.10 or 127.0.0.1)")
    send_parser.add_argument("port", type=int, help="Recipient port (e.g., 8080)")
    send_parser.add_argument("message", help="Message content (will vanish after reading or TTL)")
    send_parser.add_argument("--ttl", type=int, default=30, help="Time-to-live in seconds (default: 30)")
    send_parser.add_argument("--secret", help="Shared secret (optional; will prompt if omitted)")

    # === LISTEN ===
    listen_parser = subparsers.add_parser("listen", help="Listen for incoming bubbles")
    listen_parser.add_argument("port", type=int, help="Port to listen on (e.g., 8080)")
    listen_parser.add_argument("--secret", help="Shared secret (optional; will prompt if omitted)")

    args = parser.parse_args()

    # Get shared secret securely
    secret = args.secret
    if not secret:
        secret = getpass.getpass("🔑 Enter shared secret (hidden): ")
        if not secret:
            secret = "yourbubble_default_secret"
            print("⚠️  No secret entered. Using default (insecure for real use).")

    if args.command == "send":
        sender = BubbleSender(shared_secret=secret)
        sender.send(args.ip, args.port, args.message, args.ttl)
        print("\n✨ Bubble sent. It will vanish after being read or after TTL.")

    elif args.command == "listen":
        def handler(content):
            print(f"\n📬 New bubble: {content}")
            print("💨 The bubble has vanished.")

        listener = BubbleListener(args.port, shared_secret=secret, on_bubble=handler)
        listener.start()
        try:
            print(f"\n👂 Listening on port {args.port}... (Press Ctrl+C to stop)")
            while True:
                pass
        except KeyboardInterrupt:
            listener.stop()
            print("\n\n🛑 Listener stopped. All bubbles are gone.")

if __name__ == "__main__":
    main()