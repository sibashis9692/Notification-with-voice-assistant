from plyer import notification
import time
import pyttsx3
tittle_for_message=input("Enter the tittle of the message: ")
what_he_say=input("Enter the message: ")
notification.notify(
    title=tittle_for_message,
    message=what_he_say,
    timeout=10
)
time.sleep(2)
engine=pyttsx3.init()
engine.say(what_he_say)
engine.runAndWait()
engine.stop()