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
    # Debug print to check if bot receives messages
    print("Message received:", message.content, "Channel:", message.channel.id)

    if message.channel.id == CHANNEL_ID and not message.author.bot:
        text = f"{message.author}: {message.content}"

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        })

        print("Telegram response:", response.text)

client.run(DISCORD_TOKEN)
