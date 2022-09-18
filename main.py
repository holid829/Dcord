import os
import discord
import datetime
from datetime import timedelta
from keep_alive import keep_alive

tok = os.environ['bToken']
current_d = datetime.datetime.now()


class MyClient(discord.Client):

    async def on_ready(self):
        print('We have logged in as {0.user}.format(client)')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('plan'):
            days = message.content[4:]
            num = int(days)
            await message.channel.send('React to available dates @everyone')
            for i in range(0, num):
                msg = await message.channel.send(
                    "{:%a %d, %b %Y}".format(datetime.datetime.now() +
                                             timedelta(days=i)))
                await msg.add_reaction("✅")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

keep_alive()

client.run(tok)
