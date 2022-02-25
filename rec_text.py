from gtts import gTTS

file = "file_rec.mp3"

texto = """
Criar uma mensagem de voz grande.

muito grande.
"""

tts = gTTS(text=f'{texto}', lang='pt')
tts.save(file)
print("Pronto")
