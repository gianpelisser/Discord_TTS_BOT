import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, bot
import discord.role
import asyncio
import time
import random
import os
from gtts import gTTS
# pip install gTTS
# pip install -U discord.py[voice]
# pip install -r requirements.txt
"""
Informações sobre a Biblioteca gTTS
https://pypi.org/project/gTTS/
"""


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


intents = discord.Intents.default()
intents.message_content = True
bot = AutoShardedBot(command_prefix=".", case_insensitive=True, intents=intents)
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
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command(name='portugues', aliases=['fale', 'falar', 'f', 'tts', 'pt', 'br', 'brasil', 'brazil'])
async def tts_pt_br(ctx, *, palavra=None, channel: discord.VoiceChannel = None):
    guild = ctx.guild
    if palavra is None:
        return await ctx.send("gpt + alguma coisa")
    await ctx.send(f"Lendo sua mensagem, aguarde.")

    random_file_id = random.randint(1, 1000)
    file = f"files/file-{random_file_id}.mp3"

    try:
        user_name = ctx.author.name.lower()
        if user_name == "VORTEX" or user_name == "VORTEX UwU":
            user_name = "Vortex"
        tts = gTTS(text=f'{user_name} disse: {palavra}', lang='pt')
        tts.save(file)

    except Exception as e:
        return await ctx.send(e)

    try:
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                return await ctx.send(f"{ctx.author.mention} Você precisa estar em um canal de voz.\n"
                                      f"You need to be on a voice channel.")
        vc = ctx.voice_client
        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                pass
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                pass
        # tocar som

        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(file)
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        while voice_client.is_playing():
            time.sleep(1)

        try:
            return await ctx.voice_client.disconnect()
        except:
            return
        finally:
            os.remove(file)

    except Exception as e:
        return await ctx.send(e)
# fim pt


if __name__ == "__main__":
    bot.run(token)
