import pyttsx3 
import speech_recognition as sr
def get():
    data = input("Digite o texto que será convertido em áudio:\n")
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Agora fale no microfone o que será convertido em texto...")
        audio = r.listen(source)
        print("Feito!")

    try:
        text = r.recognize_google(audio)
        print("Você disse:\n", text)

    except Exception as e:
        print(e)

get() 

