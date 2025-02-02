# ⏳ Telegram  Bio & Name   

### 🚀 Automatically Updates Your Telegram Name & Bio Based on Real-Time Clock 🕰  

This project is a **Telegram bot** that updates your **last name and bio** every minute based on the **current time in Tehran**! 📌  

---

## ✨ Features:
- ✅ **Real-time auto-update** of last name and bio
  
- 🎨 **Multiple stylish fonts** for displaying the time
  
- 🛠 **Bot control commands:** `bot on` & `bot off`
  
- 🔐 **Secure & lightweight**—no need for an external API  

---

## 🛠 Installation & Setup

### 1️⃣ Prerequisites:
Ensure you have **Python** installed along with the required dependencies:

```bash
pip install telethon pytz
```

## 2️⃣ Obtain Telegram API Credentials:
Visit my.telegram.org
Log in with your Telegram account
Click "API Development Tools"
Generate and note your API ID and API Hash

---

### 🚀 Running the Bot
After setting up the API credentials, run the script using:

```bash
python3  main.py
```

---

### 🛠 Bot Commands:
The bot can be controlled using two simple commands:

| Command   | Functionality           |
|-----------|-------------------------|
| `bot on`  | ✅ Turns the bot ON      |
| `bot off` | ❌ Turns the bot OFF     |

---

### 📝 How It Works:
The bot fetches the current time in Tehran timezone (Asia/Tehran).
It converts the time into random stylish fonts from a predefined list.
It updates the last name and bio of your Telegram profile every 60 seconds.
You can enable or disable the bot using simple chat commands.


