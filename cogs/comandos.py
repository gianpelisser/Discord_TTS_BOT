import discord
import discord.role
from discord.ext import commands
import asyncio
from gtts import gTTS
# pip install gTTS
# pip install -U discord.py[voice]
# pip install -r requirements.txt
"""
Informações sobre a Biblioteca gTTS
https://pypi.org/project/gTTS/
"""


class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='falar', aliases=['fale', 'f'])
    async def tts(self, ctx, *, frase=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        Portugues
        """
        if frase is None:
            return await ctx.send("ttsfale + alguma coisa")
        member = ctx.author
        """ # Adicione ou remova (jogo da velha #) para desabilitar essa linha (comentar).
        # Permite usar o comando, somente quem tiver o cargo informado abaixo pelo nome (name).
        if discord.utils.find(lambda r: r.name == "Nome de um Cargo do Discord" or r.name == "Nome de um Cargo do Discord", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo sua mensagem...")
        else:
            return
        # """
        """ # Adicione ou remova (jogo da velha #) para desabilitar essa linha (comentar).
        # Bloquear outras pessoas de usar o BOT, permitindo apenas você
        if member.id != 11111:
            return
        # """
        # define um arquivo inicial para ser usado
        file = "file.mp3"

        # iniciar o TTS tts, Criar MP3 e tocar
        nome_user = str(member.name).lower()

        try:
            # Em LANG='IDIOMA' entre as aspas simples você vai colocar o Idioma que você quer.
            # Consulte a Biblioteca gTTS para ver quais são as sigles correspondentes para cada idioma.
            tts = gTTS(text=f'{nome_user} disse, {frase}', lang='pt')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)
        # Daqui indiante é fazer o BOT "tentar" entrar na mesma sala de voz que você (quem usou o comando).
        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='brazil', aliases=['pt', 'br'])
    async def ttspt(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        Portugues
        """
        if palavra is None:
            return await ctx.send("ttspt + alguma coisa")
        if discord.utils.find(lambda r: r.name == "ADM Black Holita" or r.name == "TTS [BOT]", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo sua mensagem...")
        else:
            return

        # define variables

        file = "file.mp3"

        # initialize tts, create mp3 and play
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
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)

    # fim

    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='sair', aliases=['exit', 'leave', 's'])
    async def leave(self, ctx):
        """
        Remover o BOT da CALL
        ttssair | ttss
        """
        try:
            await ctx.voice_client.disconnect()
        except:
            return
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='falaren', aliases=['faleen', 'fen', 'en'])
    async def ttsen(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        English
        """
        if palavra is None:
            return await ctx.send(".en + alguma coisa")
        if discord.utils.find(lambda r: r.name == "ADM Black Holita" or r.name == "TTS [BOT]", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo sua mensagem...")
        else:
            return

        # define variables

        file = "file.mp3"

        # initialize tts, create mp3 and play
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
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='falares', aliases=['falees', 'fes', 'es'])
    async def ttses(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        Spanish
        """
        if palavra is None:
            return await ctx.send(".es + alguma coisa")
        if discord.utils.find(lambda r: r.name == "ADM Black Holita" or r.name == "TTS [BOT]", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo sua mensagem...")
        else:
            return

        # define variables

        file = "file.mp3"

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
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='falarjp', aliases=['falejp', 'fjp', 'jp'])
    async def ttsjp(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        Japones
        """
        if palavra is None:
            return await ctx.send(".jp + alguma coisa")
        if discord.utils.find(lambda r: r.name == "ADM Black Holita" or r.name == "TTS [BOT]", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo sua mensagem...")
        else:
            return

        # define variables

        file = "file.mp3"

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
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)
    # fim

    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    @commands.guild_only()
    @commands.command(name='falarko', aliases=['faleko', 'fko', 'ko'])
    async def ttsko(self, ctx, *, palavra=None, channel: discord.VoiceChannel = None):
        """
        Entra na mesma sala de VOZ, e fala o que você escreveu.
        Koreano
        """
        if palavra is None:
            return await ctx.send(".jp + alguma coisa")
        if discord.utils.find(lambda r: r.name == "ADM Black Holita" or r.name == "TTS [BOT]", ctx.author.roles):
            # await ctx.message.delete()
            await ctx.send(f"Lendo a msg")
        else:
            return

        # define variables

        file = "file.mp3"

        # initialize tts, create mp3 and play
        try:
            tts = gTTS(text=f'{palavra}', lang='ko')
            tts.save(file)

        except Exception as e:
            return await ctx.send(e)

        try:
            if not channel:
                try:
                    channel = ctx.author.voice.channel
                except AttributeError:
                    pass
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
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file))
            return ctx.voice_client.play(source)
        except Exception as e:
            return await ctx.send(e)
    # fim


def setup(bot):
    bot.add_cog(Comandos(bot))
