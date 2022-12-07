"""Discord Bot Module"""
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import config.log as log
import config.constants as c
import controller
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

log.info("Bot has been initialized")

@bot.event
async def on_ready():
    """Prints to console that Bot has connected to Discord"""
    log.info('I have logged in!')

@bot.event
async def on_guild_join(guild):
    """Prints to console that Bot has joined a server and adds server to DB"""
    first_channel = guild.text_channels[0]
    log.info(first_channel.name)
    await send_message(first_channel,
f'Hello! Thank you for using Harmony. By default, I will be sending messages in **{first_channel.name}**')
    await send_message(first_channel,
'If you would like to change this, please use the command: &channel *channel_name*')
    controller.add_server(guild.id, first_channel)

@bot.event
async def on_guild_remove(guild):
    """Prints to console that Bot has been removed from a server and removes it from DB"""
    print(f'I have been removed from {guild.id}')
    controller.remove_server(guild.id)

@bot.command()
async def list(ctx):
    channel = ctx.channel
    guild_id = ctx.guild.id
    await a_send_message(channel, controller.list_server_info(guild_id))

@bot.command()
async def add(ctx):
    channel = ctx.channel
    guild_id = ctx.guild.id
    msg = ctx.message.content
    if msg.split(" ")[1] is not None:
        await send_message(channel, controller.add_channel(guild_id, msg.split(" ")[1]))
    else:
        await send_message(channel, c.missing_url_arg)

@bot.command()
async def remove(ctx):
    channel = ctx.channel
    guild_id = ctx.guild.id
    msg = ctx.message.content
    if msg.split(" ")[1] is not None:
        await send_message(channel, controller.remove_channel(guild_id, msg.split(" ")[1]))
    else:
        await send_message(channel, c.missing_channel_arg)

@bot.command()
async def latest(ctx):
    channel = ctx.channel
    guild_id = ctx.guild.id
    msg = ctx.message.content
    if msg.split(" ")[1] is not None:
        await send_message(channel, controller.display_channel_info(guild_id, msg.split(" ")[1]))
    else:
        await send_message(channel, c.missing_channel_arg)

@bot.command()
async def update(ctx):
    channel = ctx.channel
    await send_message(channel, controller.update_channels())

@bot.command()
async def channel(ctx):
    channel = ctx.channel
    guild_id = ctx.guild.id
    msg = ctx.message.content
    if msg.split(" ")[1] is not None:
        await send_message(channel, controller.update_discord_channel(guild_id, msg.split(" ")[1]))
    else:
        await send_message(channel, c.missing_channel_arg)  

@bot.command()
async def ping(ctx):
    log.debug("HERE IN PING")
    await send_message(ctx, "Pong")

@bot.command()
async def help_test(ctx):
    channel = ctx.channel
    await send_message(channel, c.help_text)

@bot.command()
async def pt(ctx):
    channel = ctx.channel
    # query = ctx.message.content.split(" ")[1]
    voice_channel = ctx.guild.voice_channels[0]

    vc = await voice_channel.connect()
    url = 'https://soundbytesradio.com/wp-content/uploads/1655A_ParcelTracker.mp3'
    r = requests.get(url, stream=True)
    audiosource = ()
    with r:
        for block in r.iter_content(8192):
            # print(block)
            byte = audiosource.read(block)
            vc.play(byte)
    # await send_message(channel, f"Now playing {query}")

async def send_message(channel, message):
    """Sends message to specific channel in a guild"""
    await channel.send(message)

def main():
    """Main Function"""
    load_dotenv('application\config\.env')
    discord_secret = os.getenv('DISCORD_TOKEN')
    bot.run(discord_secret)
if __name__ == '__main__':
    main()
