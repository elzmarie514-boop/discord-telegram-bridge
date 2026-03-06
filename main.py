import discord
import requests
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connected as {client.user}")

@client.event
async def on_message(message):

    if message.author.bot:
        return

    print("Message:", message.content)
    print("Channel:", message.channel.id)

    if message.channel.id == CHANNEL_ID:

        text = f"""
📨 Discord Message

👤 {message.author}

💬 {message.content}
"""

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        })

        print("Sent to Telegram")

client.run(DISCORD_TOKEN)
