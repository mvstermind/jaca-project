import argostranslate.package
import argostranslate.translate
import speech_recognition as sr


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
    # 4 is my default mic
    # use this to get what mic i have to use
    # print(sr.Microphone.list_microphone_names())
    mic_index = 4
    r = sr.Recognizer()
    print("Available microphones:", sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index=mic_index) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Sphinx thinks you said:", r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand the audio.")
    except sr.RequestError as e:
        print(f"Sphinx error: {e}")


def main():
    audio_from_mic()


if __name__ == "__main__":
    main()
