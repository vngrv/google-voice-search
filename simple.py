#!/usr/bin/env python
"""Google Cloud Speech API sample that demonstrates enhanced models
and recognition metadata.
Example usage:
    python diarization.py
"""

import argparse
import io



def transcribe_file_with_diarization():
    """Transcribe the given audio file synchronously with diarization."""
    # [START speech_transcribe_diarization_beta]
    from google.cloud import speech_v1p1beta1 as speech
    client = speech.SpeechClient()
    audio = speech.types.RecognitionAudio(uri="output/sound-2021-06-14 19:10:19.wav")

    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code='en-US',
        enable_speaker_diarization=True,
        diarization_speaker_count=2)

    print('Waiting for operation to complete...')
    response = client.recognize(config, audio)

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]

    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print("word: '{}', speaker_tag: {}".format(word_info.word,
                                                   word_info.speaker_tag))
    # [END speech_transcribe_diarization_beta]



if __name__ == '__main__':

    transcribe_file_with_diarization()