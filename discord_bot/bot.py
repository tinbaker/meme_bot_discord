import discord
import json
import requests
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = response.json()          # .json() gọn hơn json.loads(response.text)
    return json_data["url"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("/hello"):
            await message.channel.send("Hello World!")

        if message.content.startswith("/meme"):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)          # <-- không còn token trần trong code
