import speech_recognition as sr
import pyttsx3 

speech = sr.Recognizer()

#text-to-speech engine driver
try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested Driver not found')
except RuntimeError:
    print('Driver failed to initialize')

#defining voice and prinitng voice installed
voices = engine.getProperty('voices')
#printing voices installed
#for voice in voices:
#    print(voice.id)

#setting up voice rate
engine.setProperty('voice','default')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

#engine.say('Hello Sir, I am JARVIS')
#engine.runAndWait()

#command from the AI
def speak_test_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

#giving command
def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    #with microphone as source
    with sr.Microphone() as source:
    #the audio will hold the value for the speech command
        audio = speech.listen(source)

    try:  
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network Error.')
        engine.say('Sir! its seems like we have an network error')
        engine.runAndWait()
    return voice_text

if __name__ == '__main__':
    speak_test_cmd('Hello Mr. Sarkar, Am JARVIS your personal virtual assistant ')

    while True:
        voices_note ==read_voice_cmd()
        print('cmd : ()'.format(voices_note))
        gret = ['hi','hello','hey',]
        if any(elem in gret for elem in voices_note):
            speak_test_cmd()