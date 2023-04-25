import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
audio_file_ = sr.AudioFile("data/my_audio.wav")
type(audio_file)
recognizer.recognize_google(audio_data="my_audio.wav", language="en-US")