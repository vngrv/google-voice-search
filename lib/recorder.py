import pyaudio
import wave
import speech_recognition as speech_recog

from time import gmtime, strftime

class Recorder:
    '''
    Осуществляет запись звуковой дорожки.
    Запись идет на протяжении 5 секунд.

    USAGE:
        record = recorder.Recorder()
        record.start_recording().finish_recording().save_sound()
    '''
    format = pyaudio.paInt16
    rate = 44100
    channels = 1
    frame_rate = 49000
    frames_per_buffer = 1024
    frames = []
    input_device_index = 0
    seconds = 5
    microphone = None
    
    def __init__(self, save_status=False):
        if(save_status):
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format = self.format,
                rate = self.rate,
                channels = self.channels,
                frames_per_buffer = self.frames_per_buffer,
                input_device_index = 0,
                input = True
            )
        else:
            self.microphone = speech_recog.Microphone()
            pass

    def get_microphone(self):
        return self.microphone

    def get_devices_dict(self):
        return [{ i: self.p.get_device_info_by_index(i)['name']} for i in range(self.p.get_device_count())]

    def start_recording(self):
        self.print_message('Start Recording...')
        for i in range(0, int(self.rate / self.frames_per_buffer * self.seconds)):
            data = self.stream.read(self.frames_per_buffer)
            self.frames.append(data)

        return self

    def finish_recording(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.print_message('Finished recording.')

        return self

    def save_sound(self):
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        wf = wave.open("output/sound-" + time + ".wav", 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.frame_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        return self

    def print_message(self, message):
        print(message)

