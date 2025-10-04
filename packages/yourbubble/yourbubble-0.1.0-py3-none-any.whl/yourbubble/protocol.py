#!/usr/bin/env python3
"""
yourbubble.protocol v0.1
Ephemeral UDP messaging with VeilCipher — zero dependencies, full transparency.
Philosophy: "The bubble exists only while it is needed."
"""

import socket
import threading
import time
import json
import os
import hashlib
import base64
import struct
from typing import Optional, Callable

# ────────────────────────────────
# 🔐 VeilCipher — your own crypto, no dependencies
# ────────────────────────────────

def _stretch_key(secret: str, salt: bytes, length: int = 64) -> bytes:
    try:
        h = hashlib.sha3_256()
    except AttributeError:
        h = hashlib.sha256()
    h.update(secret.encode() + salt)
    key = h.digest()
    while len(key) < length:
        h = h.copy()
        h.update(key[-32:])
        key += h.digest()
    return key[:length]

def _prf(key: bytes, counter: int) -> bytes:
    h = hashlib.sha256()
    h.update(key)
    h.update(struct.pack("<Q", counter))
    return h.digest()

class VeilCipher:
    @staticmethod
    def encrypt(plaintext: str, secret: str) -> str:
        plaintext_bytes = plaintext.encode("utf-8")
        nonce = os.urandom(16)
        salt = nonce[:8]
        key = _stretch_key(secret, salt, length=48)
        keystream = b""
        counter = 0
        while len(keystream) < len(plaintext_bytes):
            keystream += _prf(key[:32], counter)
            counter += 1
        keystream = keystream[:len(plaintext_bytes)]
        ciphertext = bytes(a ^ b for a, b in zip(plaintext_bytes, keystream))
        packet = nonce + ciphertext
        return base64.urlsafe_b64encode(packet).decode("ascii").rstrip("=")

    @staticmethod
    def decrypt(encrypted_b64: str, secret: str) -> str:
        pad = "=" * ((4 - len(encrypted_b64) % 4) % 4)
        packet = base64.urlsafe_b64decode(encrypted_b64 + pad)
        if len(packet) < 16:
            raise ValueError("Packet too short")
        nonce = packet[:16]
        ciphertext = packet[16:]
        salt = nonce[:8]
        key = _stretch_key(secret, salt, length=48)
        keystream = b""
        counter = 0
        while len(keystream) < len(ciphertext):
            keystream += _prf(key[:32], counter)
            counter += 1
        keystream = keystream[:len(ciphertext)]
        plaintext_bytes = bytes(a ^ b for a, b in zip(ciphertext, keystream))
        return plaintext_bytes.decode("utf-8")

# ────────────────────────────────
# 🌊 Bubble
# ────────────────────────────────

class Bubble:
    def __init__(self, content: str, ttl: int = 30):
        self.content = content
        self.ttl = ttl
        self.created_at = time.time()
        self.read = False

    def is_expired(self) -> bool:
        return time.time() > self.created_at + self.ttl

    def read_content(self) -> Optional[str]:
        if self.is_expired():
            return None
        self.read = True
        return self.content

    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "ttl": self.ttl,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Bubble":
        bubble = cls(data["content"], data["ttl"])
        bubble.created_at = data["created_at"]
        return bubble

# ────────────────────────────────
# 📡 BubbleSender
# ────────────────────────────────

class BubbleSender:
    def __init__(self, shared_secret: str = "yourbubble_default_secret"):
        self.shared_secret = shared_secret

    def send(self, host: str, port: int, content: str, ttl: int = 30):
        bubble = Bubble(content, ttl)
        payload = json.dumps(bubble.to_dict())
        encrypted = VeilCipher.encrypt(payload, self.shared_secret)
        packet = {"v": "2", "veil": encrypted}
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(json.dumps(packet).encode(), (host, port))
            print(f"🌊 Bubble sent to {host}:{port} (🔒 VeilCipher, TTL={ttl}s)")
        finally:
            sock.close()

# ────────────────────────────────
# 📥 BubbleListener
# ────────────────────────────────

class BubbleListener:
    def __init__(self, port: int, shared_secret: str = "yourbubble_default_secret", on_bubble: Optional[Callable] = None):
        self.port = port
        self.shared_secret = shared_secret
        self.on_bubble = on_bubble or self._default_handler
        self._running = False

    def _default_handler(self, content: str):
        print(f"📬 Bubble received: {content}")
        print("💨 The bubble has vanished.")

    def start(self):
        self._running = True
        thread = threading.Thread(target=self._listen, daemon=True)
        thread.start()
        print(f"👂 Listening on port {self.port}...")

    def _listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", self.port))
        # Flush old packets
        sock.settimeout(0.1)
        try:
            while True:
                sock.recvfrom(4096)
        except socket.timeout:
            pass
        sock.settimeout(None)

        while self._running:
            try:
                data, addr = sock.recvfrom(4096)
                packet = json.loads(data.decode())
                if packet.get("v") == "2":
                    try:
                        payload_str = VeilCipher.decrypt(packet["veil"], self.shared_secret)
                        payload = json.loads(payload_str)
                        bubble = Bubble.from_dict(payload)
                        if bubble.is_expired():
                            print("⏳ Bubble expired.")
                        else:
                            content = bubble.read_content()
                            if content:
                                self.on_bubble(content)
                    except Exception as e:
                        print(f"❌ Decryption failed: {e}")
                else:
                    print("❓ Unsupported protocol version")
            except Exception as e:
                if self._running:
                    print(f"⚠️  Error: {e}")

    def stop(self):
        self._running = False

# ────────────────────────────────
# 🧪 Test
# ────────────────────────────────

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python protocol.py send|listen")
        sys.exit(1)

    SECRET = "yourbubble_default_secret"

    if sys.argv[1] == "listen":
        listener = BubbleListener(8080, SECRET)
        listener.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            listener.stop()
            print("\n🛑 Listener stopped.")

    elif sys.argv[1] == "send":
        sender = BubbleSender(SECRET)
        sender.send("127.0.0.1", 8080, "Hello from your own bubble!", ttl=10)