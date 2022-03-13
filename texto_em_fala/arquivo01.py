import pyttsx3

#Carrega a lib
engine = pyttsx3.init()

# Textos que será falado
engine.say("Ola mundo")
engine.say("Programar em Python")

# executa
engine.runAndWait()