from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import AutoShardedBot
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

modulos = ["cogs.comandos"]

bot = AutoShardedBot(command_prefix="tts", case_insensitive=True)
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

    # await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=f"Meme Song"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    await bot.process_commands(message)


if __name__ == "__main__":
    for modulo in modulos:
        bot.load_extension(modulo)

    bot.run(token)
