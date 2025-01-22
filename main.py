from audio import transcription
from personality import Jaca
import pyttsx3
import sys


# def scroll_reels():
#     import pyautogui
#     pyautogui.scroll(-100000000000000)


def main():
    transcribed_text = ""
    if sys.argv[1] == "wokal":
        transcribed_text = transcription.audio_from_mic()

    elif sys.argv[1] == "text":
        transcribed_text = sys.argv[1:]

    output = transcription.translate(
        transcribed_text, source_lang="pl", output_lang="en"
    )
    # tell me what i said
    print(f"{output}\n")

    jaca = Jaca(output=output)
    resp = jaca.response()
    if resp is not None:
        jaca_pl = transcription.translate(resp, source_lang="en", output_lang="pl")
        engine = pyttsx3.init()

        # u need to download any of voices, figure out how to make it on every system
        # this is to find voices available
        # voices = engine.getProperty("voices")
        # for voice in voices:
        #     print(
        #         f"Voice ID: {voice.id}, Name: {voice.name}, Language: {voice.languages}"
        #     )

        print(jaca_pl)
        engine.setProperty("voice", "com.apple.voice.compact.pl-PL.Zosia")
        engine.say(jaca_pl)
        engine.runAndWait()


# scroll_reels()


if __name__ == "__main__":
    main()
