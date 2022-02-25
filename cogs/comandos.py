import discord
import discord.role
from discord.ext import commands
import asyncio
import time
import random
import os
from gtts import gTTS
"""
from pygame import mixer
import os
import json
import pymysql
import pymysql.cursors
import ffmpeg
from youtube_dl import YoutubeDL
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
# pip install --upgrade discord-components
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption
)
"""


class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='portugues', aliases=['fale', 'falar', 'f', 'tts', 'pt', 'br', 'brasil', 'brazil'])
    async def tts_pt_br(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("gpt + alguma coisa")
        await ctx.send(f"Lendo sua mensagem, aguarde.")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        try:
            tts = gTTS(text=f'{palavra}', lang='pt')
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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

    # fim

    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='exit', aliases=['sair', 's', 'leave'])
    async def leave_cmd(self, ctx):
        """
        Remove BOT from the Call (Sala de Voz).
        """
        try:
            await ctx.voice_client.disconnect()
        except:
            return
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='english', aliases=['en', 'eng', 'ingles'])
    async def tts_eng(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("gen + text")

        await ctx.send(f"Reading your message, wait...")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        try:
            tts = gTTS(text=f'{palavra}', lang='en')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send(f"{ctx.author.mention} You need to be on a voice channel.")
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='espanhol', aliases=['esp', 'es'])
    async def tts_esp(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("ges + text")
        await ctx.send(f"Leyendo tu mensaje, espera...")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        # initialize tts, create mp3 and play
        try:
            tts = gTTS(text=f'{palavra}', lang='es')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send(f"{ctx.author.mention} Tienes que estar en un canal de voz.\n"
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='japanese', aliases=['ja', 'jp'])
    async def ttsjp(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("gjp + text")
        await ctx.send(f"待ってください。")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        # initialize tts, create mp3 and play
        try:
            tts = gTTS(text=f'{palavra}', lang='ja')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send(f"{ctx.author.mention} You need to be on a voice channel.\n"
                                          f"音声チャネルを使用する必要があります。")
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='coreano', aliases=['koreano', 'ko', 'co'])
    async def ttsko(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("gko + text")
        await ctx.send(f"메시지를 읽는 중, 잠시만")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        # initialize tts, create mp3 and play
        try:
            # tts = gTTS(text=f'{nome} disse, {palavra}', lang='pt')
            tts = gTTS(text=f'{palavra}', lang='ko')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send(f"{ctx.author.mention} You need to be on a voice channel.\n"
                                          f"음성 채널에 있어야 합니다.")
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='german', aliases=['ge', 'al', 'de', 'Deutschland'])
    async def ttsde(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        guild = ctx.guild
        if palavra is None:
            return await ctx.send("gde + text")
        await ctx.send(f"Warten Sie mal.")

        random_file_id = random.randint(1, 1000)
        file = f"files/file-{random_file_id}.mp3"

        # initialize tts, create mp3 and play
        try:
            tts = gTTS(text=f'{palavra}', lang='de')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    return await ctx.send(f"{ctx.author.mention} You need to be on a voice channel.\n"
                                          f"Sie müssen sich in einem Sprachkanal befinden.")
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

            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
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
    # fim

    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='rec', aliases=['record'])
    async def gravar(self, ctx):
        await ctx.send(f"{ctx.author.mention} Iniciando Gravação.")
        file = "record.mp3"

        texto = """
Olá, bem-vindo!
Deixa o like e inscreva-se no canal.
Neste vídeo, vamos consertar esse trânsito infernal que você está vendo no vídeo.

E como não sou muito "falador", para ajudar o áudio da gravação deu problema, e é por isso que só temos uma música de fundo e esse áudio do google tradutor.

Bem, o começo do vídeo é só a correção do trânsito e somente depois coloquei o video em alta velocidade para que você possa aproveitar o rápido crescimento da cidade.

Me diga o que você está pensando desta cidade, eu acho que está ficando muito bonita, e acredito que ficará muito mais, deixa seu comentário.
        """

        tts = gTTS(text=f'{texto}', lang='pt')
        tts.save(file)
        print("Pronto")
        await ctx.send(f"{ctx.author.mention} Pronto")
    # fim


def setup(bot):
    bot.add_cog(Comandos(bot))
