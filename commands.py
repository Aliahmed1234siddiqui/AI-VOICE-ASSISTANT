#  region Modules Calling
from modules.WebBrowserFunction import  open_website
from modules.MusicPlayer import play_music 
from modules.ChatgptSerach import chat_with_ai
from modules.SystemControl import control_pc  
from modules.WikiPediaSerach import search_wikipedia 
from modules.WeatherNews import get_weather
import speech_recognition as sr
import pyttsx3




# region  Text-to-Speech 
engine = pyttsx3.init()



# region  Speech Recognizer
recognizer = sr.Recognizer()

# region speak function 
def speak(text):    
    """Convert text to speech and speak it."""
    engine.say(text)
    engine.runAndWait()

# region Voice Recognition function
def listen():
    """Recognize and return voice input as text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't understand."
    except sr.RequestError:
        return "Could not connect to the speech recognition service."




# region main function
def main():
    speak("Hello! How can I assist you today?")
    paused = False

    while True:
        command = listen()
        # ye basically hold karne ka option  hn 
        if "wait" in command:
            paused = True
            speak("Okay, I will wait. Say 'continue' when you're ready.")
            continue

        # ye basically continune akrne ka option hn  
        if paused:
            if "continue" in command:
                paused = False
                speak("I'm back. How can I help you?")
            else:
                continue  
            continue

        # ye basically exit or server band  karne ka option hn  
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        # ye basically website open karne ka option hn karne ka option hn  
        # open kay word per kam karta hn or ye model bassed agent hn 

        elif "open" in command:
            result = open_website(command)

# is se wikipedia serach huga modal baesd agent hn na y
        elif "wikipedia" in command:
            result = search_wikipedia(command)

        elif "chat" in command: 
            prompt = command.replace("chat", "").strip()
            result = chat_with_ai(prompt)

            # os wala cammand handle kar raha hn

        elif "shutdown" in command or "restart" in command or "kholo" in command:
            result = control_pc(command)
            # working with api of weather
        elif "weather" in command:
            city = command.replace("weather", "").strip()
            print(city)
            result = get_weather(city)

            # for play music 
        elif "play music" in command:
            result = play_music()
        else:
            result = "I don't understand that command."
        print(result)
        speak(result)




# region calling main  function 


#  ye asa built-in ariable hn jo script agar direct call hu tu bss jab chalta hn 
if __name__ == "__main__":
    main()
