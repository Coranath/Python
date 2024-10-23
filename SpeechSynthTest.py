import pyttsx3

voiceEngine = pyttsx3.init()

voices = voiceEngine.getProperty('voices')

for voice in voices:
    voiceEngine.setProperty('voice', voice.id)
    print(f'Voice: {voice.id}\n {voice.name}')
    voiceEngine.say("Hello world! This is my first shot at a voice for Djinn")

voiceEngine.runAndWait()



