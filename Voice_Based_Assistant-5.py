import speech_recognition as sr
import webbrowser

print("Welcome")

r = sr.Recognizer()

with sr.Microphone() as source : # 'with' keyword is used to connect Python with Microphone and store the variable named as 'source '
    print("Start Saying, we are listening....")
    audio  =r.listen(source) # listen() will listen the voice and store into the variable named as 'audio'
    print("We got your requirement, please Wait!")

ch = r.recognize_google(audio)

if (("run" or "start" or "launch") and ("Linux" in ch)):
	webbrowser.open("http://Your IP Address/mypage.html")
elif (("exit" or "quit") in ch):
	exit()
else:
	print("Wrong choice")
