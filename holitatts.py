from discord.ext import commands
from discord.ext.commands import AutoShardedBot, bot
"""
import os
from discord.voice_client import VoiceClient
import discord
import discord.role
import json
import asyncio
import pymysql
import pymysql.cursors
import valve.source
import valve.source.a2s
import valve.source.master_server
# pip install --upgrade discord-components
from discord_components import (
    DiscordComponents,
    ComponentsBot
)
"""


def read_token():
    with open("token_holita1.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

modulos = ["cogs.comandos"]

bot = AutoShardedBot(command_prefix=["g", "G"], case_insensitive=True)
'''bot = ComponentsBot(command_prefix=["g", "G"], case_insensitive=True)
DiscordComponents(bot)'''
# bot.remove_command('help')


@bot.listen("on_command_error")
async def error_handler(ctx, error):
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandOnCooldown):
        s = error.retry_after
        s = round(s, 2)
        h, r = divmod(int(s), 3600)
        m, s = divmod(r, 60)
        return await ctx.send(f'Cooldown você precisa esperar **{str(h) + "h : " if h != 0 else ""}{str(m) + "m : " if m != 0 else ""}{str(s) + "s" if s != 0 else ""}** para usar esse comando novamente.')


@bot.event
async def on_ready():
    print('-=-' * 24)
    print(f"BOT: {bot.user.name} | Online.")
    print(f"ID: {bot.user.id}")
    print('-=-' * 10, '[ Vortex ]', '-=-' * 10)
    print('-=-= [ TTS ] =-=-')


@bot.event
async def on_message(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content:
        member = message.author

        return await message.channel.send(f"{member.mention} Você me mencionou? | Did you mention me?\n"
                                          f"Meu prefixo é | My prefix is:\n"
                                          f"**g**")
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    await bot.process_commands(message)


if __name__ == "__main__":
    for modulo in modulos:
        bot.load_extension(modulo)

    bot.run(token)
