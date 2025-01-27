import torch
import faiss
from TTS.api import TTS
import librosa
import numpy as np
import soundfile as sf


class RVCModel(torch.nn.Module):
    def __init__(self):
        super(RVCModel, self).__init__()
        self.layer1 = torch.nn.Linear(128, 128)


def synthesize_speech(
    text,
    tts_model_name="tts_models/en/ljspeech/tacotron2-DDC",
    output_path="tts_output.wav",
):
    tts = TTS(model_name=tts_model_name, progress_bar=True, gpu=False)

    tts.tts_to_file(text=text, file_path=output_path)
    print(f"Synthesized speech saved as: {output_path}")
    return output_path


def preprocess_audio(input_audio, sample_rate=40000):
    audio, sr = librosa.load(input_audio, sr=None, mono=True)

    if sr != sample_rate:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=sample_rate)

    return audio, sample_rate


def load_rvc_model(model_path, index_path):
    # Instantiate your model architecture first
    model = RVCModel()  # Replace with your actual model class name

    # Load the weights into the model
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()  # Set the model to evaluation mode

    index = faiss.read_index(index_path)

    print(f"Model loaded from {model_path} and FAISS index loaded from {index_path}.")

    return model, index


def rvc_conversion(model, index, input_audio, output_audio, sample_rate=40000):
    audio, _ = preprocess_audio(input_audio, sample_rate)
    audio = audio / np.max(np.abs(audio))
    audio_tensor = torch.from_numpy(audio).unsqueeze(0).float()

    with torch.no_grad():
        # Apply RVC model conversion to the audio tensor
        converted_audio = model(audio_tensor, index)

    # Save the converted audio
    sf.write(output_audio, converted_audio.squeeze(0).numpy(), samplerate=sample_rate)

    print(f"Conversion complete! Audio saved as: {output_audio}")
    return output_audio


def convert_text_to_target_voice(
    text,
    tts_model_name="tts_models/en/ljspeech/tacotron2-DDC",
    tts_output="tts_output.wav",
    model_path="weights/KB_Komputer_RIN_E3.pth",
    index_path="weights/added_IVF79_Flat_nprobe_1_KB_Komputer_RIN_E3_v2.index",
    rvc_output="final_output.wav",
):
    cleared_text = preprocess_polish_text(text)
    tts_output_path = synthesize_speech(cleared_text, tts_model_name, tts_output)
    model, index = load_rvc_model(model_path, index_path)
    rvc_output_path = rvc_conversion(model, index, tts_output_path, rvc_output)

    return rvc_output_path


def preprocess_polish_text(text):
    polish_characters = {
        "ć": "c",
        "ó": "o",
        "ż": "z",
        "ś": "s",
        "ą": "a",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ź": "z",
    }

    for char, replacement in polish_characters.items():
        text = text.replace(char, replacement)

    return text
