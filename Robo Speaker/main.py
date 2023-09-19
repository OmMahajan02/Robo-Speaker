import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

text = input("Enter what you want to listen: ")
speak.Speak(text)

