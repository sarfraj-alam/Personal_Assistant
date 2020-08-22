import os
import pyttsx3

print("\n\n  Can you tell me your name : ", end='')
name = input()

while (True):
	print("\n\t\t\t\t --------------- WELCOME", name.upper(), "---------------")
	print("\n\t\t\t\tFollowing OS Based Programs you can Launch : \n")
	print("\t\t\t\t1. Microsoft Edge")
	print("\t\t\t\t2. Notepad ")
	print("\t\t\t\t3. Window Media Player\n")

	print("  Which OS Based Program You Want to Launch : "  , end='')
	user_query = input()

	if (user_query != user_query.upper()):
		user_query = user_query.upper()
	else:
		pass

	if ( ("DO NOT" in user_query) or ("DON'T" in user_query) ):
		print("  Okay! We are not opening")

	elif ( ( ("RUN" in user_query) or ("START" in user_query) or ("EXECUTE" in user_query) or ("LAUNCH" in user_query) or ("OPEN" in user_query) ) and ("EDGE" in user_query) ):
		pyttsx3.speak("Opening Microsoft Edge")
		os.system("msedge")

	elif ( ( ("RUN" in user_query) or ("START" in user_query) or ("EXECUTE" in user_query) or ("LAUNCH" in user_query) or ("OPEN" in user_query) ) and ( ("NOTEPAD" in user_query)
	or ("EDITOR" in user_query) or ("TEXT EDITOR" in user_query) ) ):
		pyttsx3.speak("Opening Notepad")
		os.system("notepad")

	elif ( ( ("RUN" in user_query) or ("START" in user_query) or ("EXECUTE" in user_query) or ("LAUNCH" in user_query) or ("OPEN" in user_query) ) and ( ("MEDIA" in user_query)
	 or ("PLAYER" in user_query) or ("MEDIA PLAYER" in user_query) ) ):
		pyttsx3.speak("Opening Windows Media Player")
		os.system("wmplayer")

 
	elif ( ("QUIT" in user_query) or ("EXIT" in user_query) ):
		pyttsx3.speak("Thanks for using! Hope you like this personal assistant")
		break

	else:
		print("We do not support", user_query, "program")