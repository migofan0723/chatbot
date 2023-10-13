from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response_3_5_turbo

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as ", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        command, user_message = None, None
        for text in ['/ai_turbo']:
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message = message.content.replace(text, '')

                if command == '/ai_turbo':
                    bot_response = chatgpt_response_3_5_turbo(prompt = user_message)
                    await message.channel.send(bot_response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)