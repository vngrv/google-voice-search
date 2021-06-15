from lib import recorder, eraser, requester
import traceback
import pyaudio
import speech_recognition as speech_recog
# import speech_recognition as sr

if __name__ == '__main__':
    record = recorder.Recorder()
    request = requester.Requester()
    erase = eraser.Eraser()

    # erase.print_path()
    # erase.execute()

#    #import library
#     import speech_recognition as sr

#     # Initialize recognizer class (for recognizing the speech)
#     r = sr.Recognizer()

#     # Reading Audio file as source
#     # listening the audio file and store in audio_text variable

#     with sr.AudioFile('output/sound-2021-06-14--19:10:19.wav') as source:
    
#         audio_text = r.listen(source)
        
#         # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#         try:
            
#             # using google speech recognition
#             text = r.recognize_google(audio_text)
#             print('Converting audio transcripts into text ...')
#             print(text)
        
#         except Exception as e:
#             print('Ошибка:\n', traceback.format_exc())
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    speech_recog.Microphone.list_microphone_names()
    with mic as audio_file:
        print("Speak Please")

        recog.adjust_for_ambient_noise(audio_file, )
        audio = recog.listen(audio_file, timeout=3)

        print("Converting Speech to Text...")
        print("You said: ")
        print(recog.recognize_google(audio, language="ru-RU", show_all=True))
