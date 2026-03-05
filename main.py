import discord
import requests
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connected as {client.user}")

@client.event
async def on_message(message):

    print("Message received:", message.content, "Channel:", message.channel.id)

    if message.channel.id == CHANNEL_ID:
        text = f"{message.author}: {message.content}"

        print("Sending to Telegram:", text)

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        r = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        })

        print("Telegram response:", r.text)

client.run(DISCORD_TOKEN)
