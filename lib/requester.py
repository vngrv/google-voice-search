import speech_recognition as speech_recog

class Requester:
    recognizer = None
    audio = None
    parsed_words = None

    def __init__(self) -> None:
        self.recognizer = speech_recog.Recognizer()
    
    def get_audio(self, audio_file):
        self.recognizer.adjust_for_ambient_noise(audio_file)
        self.audio = self.recognizer.listen(audio_file, timeout=3)

        return self

    def parse_words(self):
        self.parsed_words = self.recognizer.recognize_google(self.audio, language="ru-RU", show_all=True)
        print(self.parsed_words)

        return self

    def print_message(self, message):
        print(message)

        return self

    def print_state(self):
        pass
        
        
    
    