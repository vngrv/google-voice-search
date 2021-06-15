from lib import recorder, requester, command

if __name__ == '__main__':

    record = recorder.Recorder()
    microphone = record.get_microphone()

    googleWordParser = requester.Requester()

    with microphone as audio_file:

        googleWordParser.print_message("Speak Please.")

        googleWordParser.recognizer.adjust_for_ambient_noise(audio_file)
        audio = googleWordParser.recognizer.listen(audio_file, timeout=3)

        googleWordParser.print_message("Converting. Please wait.").print_message("You said: ")

        result = googleWordParser.recognizer.recognize_google(audio, language="ru-RU", show_all=True)

        cmd = command.Command(result)
        cmd.define_command().call_command().print_command()

