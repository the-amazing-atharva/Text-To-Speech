import os  # MacOS
import win32com.client as wincom  # Windows

if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to RoboSpeaker")
    print()
    contin = True
    while contin:
        word = input("Enter what you want to say: ")
        if word == "q":
            break
        # For Windows:
        speak.Speak(word)
        # For MacOS:
        # command = f"say {word}"
        # os.system(command)
