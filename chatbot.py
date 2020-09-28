#import pyttsx3,pyaudio
"""import speech_recognition


speech_engine = pyttsx3. init('sapi5' ) # veja http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		#return recognizer.recognize_sphinx(audio)
		 #or
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Não foi possível entender o áudio")
	except speech_recognition.RequestError as e:
		print("Erro de reconhecimento; {0}".format(e))

	return speak('Não entendi o que você falou , você pode repetir?')

speak("Olá, meu nome é Bia ")

speak("Eu ouvi você dizer " + listen())

"""

import os,sys
import speech_recognition as sr
import speech_recognition
from gtts import gTTS
import pyttsx3
from playsound import playsound
import pyaudio

speech_engine = pyttsx3.init('sapi5' ) # veja http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

#Funcao responsavel por falar
def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    # Salva o arquivo de audio
    tts.save('C:/Users/x1ibn/PycharmProjects/meuChatbot/hello.mp3')
    speak("Estou aprendendo o que você disse...")
    print("Estou aprendendo o que você disse...")
    # Da play ao audio
    playsound('C:/Users/x1ibn/PycharmProjects/meuChatbot/hello.mp3')

# Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)


    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Após alguns segundos, retorna a frase falada

        print("Você disse: " + frase)
    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except speech_recognition.UnknownValueError:
            print("Não entendi")
    return frase

speak('Meu nome é Bia ')
speak('diga alguma coisa ')
frase = ouvir_microfone()

cria_audio(frase)

#"""