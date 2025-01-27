import sys
import os
from vosk import Model, KaldiRecognizer
import pyaudio


def listen():
    if not os.path.exists("model"):
        print(
            "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder."
        )
        sys.exit(1)

    model = Model("model")

    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()

    stream = mic.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8000,
    )

    print("listening")

    while True:
        result = ""
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            break

    return format_json(input=result)


def format_json(input: str) -> str:
    return input[14:-3]
