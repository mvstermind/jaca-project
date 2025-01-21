import argostranslate.package  # pyright: ignore[reportMissingImports]
import argostranslate.translate  # pyright: ignore[reportMissingImports]
import wave
import os
import whisper
import speech_recognition as sr

model = whisper.load_model("small")


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


def audio_from_mic() -> str:
    mic_index = 4  # adjust this if needed (check mic index with sr.Microphone.list_microphone_names())
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)

    try:
        # save the audio data to a WAV file
        filename = "file.wav"

        wav_data = audio.get_wav_data()  # pyright: ignore[reportAttributeAccessIssue]
        with wave.open(filename, "wb") as wav_file:
            wav_file.setnchannels(1)  # mono this shit
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            wav_file.writeframes(wav_data)

        print(f"Audio successfully written to {filename}")

        transcription = transcribe_wav(filename)

        os.remove(filename)

        return transcription

    except Exception as e:
        print(f"Error while writing audio: {e}")


def transcribe_wav(filename: str) -> str:
    result = model.transcribe(filename)
    return result["text"]  # pyright: ignore[reportReturnType]
