# 🌊 yourbubble  
*Ephemeral messaging over UDP — send, receive, vanish.*

> "The bubble exists only while it is needed."

## 🌿 Philosophy
- **No servers. No logs. No traces.**  
- Messages **self-destruct** after reading or TTL.  
- **Zero dependencies** — pure Python stdlib.  
- **Transparent crypto** — auditable, not magical.

## ✨ Features
- 🔒 **VeilCipher**: your own lightweight, dependency-free encryption  
- ⏳ **Time-to-live (TTL)**: bubbles vanish automatically  
- 📡 **UDP-based**: no persistent connection, no metadata  
- 💬 **CLI-first**: simple, scriptable, human

## 🚀 Quick Start

### Install
```bash'''
pip install yourbubble

# Listen for bubbles

yourbubble listen 8080
# → Enter shared secret when prompted

# Send a bubble

yourbubble send 192.168.1.10 8080 "This will vanish" --ttl 30
# → Enter the same shared secret

🔑 The shared secret is never transmitted. It must be exchanged securely (e.g., in person, via QR, etc.). 

📜 License
MIT — but used with intention.

Part of a quiet rebellion against digital permanence.