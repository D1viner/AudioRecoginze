import speech_recognition as sr

recording = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    recording.adjust_for_ambient_noise(source)
    print("Please Say something:")
    audio = recording.listen(source, timeout=3, phrase_time_limit=3)

try:
    print("You said: \n" + recording.recognize_sphinx(audio))
except Exception as e:
    print(e)
