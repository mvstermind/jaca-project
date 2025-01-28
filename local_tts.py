from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import torch
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/pl/mai_female/vits", progress_bar=False).to(device)

# filenames
ORIGINAL_TTS = "tts.wav"


def read(text_input: str):
    tts.tts_with_vc_to_file(
        text=text_input,
        speaker_wav="tts_voice/speaker.wav",
        file_path=ORIGINAL_TTS,
    )

    audio = AudioSegment.from_wav(ORIGINAL_TTS)
    audio = audio.speedup(playback_speed=1.1)
    audio.export(ORIGINAL_TTS, format="wav")

    os.remove(ORIGINAL_TTS)
    play(audio)
