import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = open("token.txt", "r").read()


@client.event 
async def on_connect():
    print("Connected!")


@client.event
async def on_message(message):
    if message.content.startswith("$neutralbot"):
        await message.channel.send("Hello! You said:" + message.content[11:])

client.run(TOKEN)