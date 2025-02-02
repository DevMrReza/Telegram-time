from datetime import datetime
from random import choice
from telethon import TelegramClient, functions, events
import asyncio
import pytz


api_id = YOUR_API_ID  
api_hash = "YOUR_API_HASH"


time_zone = pytz.timezone("Asia/Tehran")


fonts = [
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "❶", "❷", "❸", "❹", "➄", "➅", "➆", "❽", "❾"],
]


client = TelegramClient("ALPHATRICK", api_id, api_hash)

bot_active = True  

async def change_name():
    global bot_active
    while True:
        if bot_active:
            font = choice(fonts)  
            table = str.maketrans("0123456789", "".join(font))
            time = datetime.now(time_zone).strftime("%H:%M").translate(table)
            bio_text = f"⏱ ساعت {time} می‌باشد."

            try:
                if not await client.is_user_authorized():
                    print("[ERROR] Client is not authorized!")
                    break  

                await client(functions.account.UpdateProfileRequest(last_name=time, about=bio_text))
                print(f"[UPDATED] Last Name: {time} | Bio: {bio_text}")
            except Exception as e:
                print(f"[ERROR] {e}")

        await asyncio.sleep(60)

@client.on(events.NewMessage(pattern="bot off"))
async def bot_off(event):
    global bot_active
    bot_active = False
    await event.reply("✅ ربات خاموش شد!")

@client.on(events.NewMessage(pattern="bot on"))
async def bot_on(event):
    global bot_active
    bot_active = True
    await event.reply("✅ ربات روشن شد!")

async def main():
    if not client.is_connected():
        await client.start()
    
    print("Bot Started")
    await change_name()

with client:
    client.loop.run_until_complete(main())
