import argostranslate.package
import argostranslate.translate
import speech_recognition as sr
import os
import wave

file_index = 0


def translate(text: str, source_lang: str, output_lang: str) -> str:
    from_code = source_lang
    to_code = output_lang

    # for now keep it, l8 remove it
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code,
            available_packages,
        )
    )

    argostranslate.package.install_from_path(package_to_install.download())

    translatedText = argostranslate.translate.translate(text, from_code, to_code)
    return translatedText


def audio_from_mic():
    mic_index = 4  # adjust this if needed (check mic index with sr.Microphone.list_microphone_names())
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)

    try:
        # save the audio data to a WAV file
        global file_index
        filename = f"file_{file_index}.wav"
        wav_data = audio.get_wav_data()
        with wave.open(filename, "wb") as wav_file:
            wav_file.setnchannels(1)  # mono this shit
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            wav_file.writeframes(wav_data)

        print(f"Audio successfully written to {filename}")
        file_index += 1

    except Exception as e:
        print(f"Error while writing audio: {e}")


def main():
    audio_from_mic()


if __name__ == "__main__":
    main()
