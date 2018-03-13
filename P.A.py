from gtts import gtts
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTs(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens for commands

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('you said: ' + command + '/n')

    #loop back to continue to listen for commands

    except sr.UnknowValueError:
        assistant(myCommand())

    return command

#if statements for executing commands
def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)





    if 'is Jeffrey gay?' in command:
        talkToMe('nope he is totaly straight')



    if 'is Jeffrey Stupid?' in command:
        talkToMe("I don't think so my master is the smartest person in this room")


    if 'whats up' in command:
        talkToMe('Chillin bro')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('what should i say')
            content = myCommand()

            #init gmail smtp
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message

            mail.sendmail('PERSON NAME', 'jeffreylode2310@gmail.com', content)

            #close connection

            mail.close()

            talkToMe('your email has been sent')




talkToMe('I am ready for your command')

            if else

            talkToMe('I will search on the internet')

            chrome_path = '/usr/bin/google-chrome'
            url = ('http://' + command)
            webbrowser.get(chrome_path).open(url)

while True:

    assistant(myCommand())
