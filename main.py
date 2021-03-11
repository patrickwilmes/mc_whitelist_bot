import discord
import configparser

from mc.constants import SERVER_WHITELIST_TARGET_KEY, SERVER_CONFIG_SECTION, DISCORD_CONFIG_SECTION, \
    DISCORD_TOKEN_FILE_KEY
from mc.message_handler import handle_message
from mc.whitelist_handler import WhitelistHandler

config = configparser.ConfigParser()
config.read('config.ini')

handler = WhitelistHandler(config)

client = discord.Client()


@client.event
async def on_ready():
    print('bot started successfully')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(handle_message(message.content, handler))

if __name__ == '__main__':
    with open(config[DISCORD_CONFIG_SECTION][DISCORD_TOKEN_FILE_KEY]) as file:
        token = file.readline()
        client.run(token)
