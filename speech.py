import time

import speech_recognition as sr


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Did you said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

MICROPHONE_INDEX = 0
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
MICROPHONE_INDEX=int(input("Which microphone do you want to use?")) 
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
mic = sr.Microphone(device_index=MICROPHONE_INDEX)
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
stop_listening = recognizer.listen_in_background(mic, callback)
    # audio = recognizer.listen(source)
input("press any key to exit")
# print(recognizer.recognize_google(audio))

