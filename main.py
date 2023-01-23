import speech_recognition as speech


rec = speech.Recognizer()

with speech.Microphone() as voice:
    print('Say')
    audio = rec.listen(voice)
    try:
        print('You say' + rec.recognize_google(audio))
    except:
        print('SORRY')