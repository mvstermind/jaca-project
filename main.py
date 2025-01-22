from audio import transcription
from personality import Jaca


def main():
    transcribed_text = transcription.audio_from_mic()
    output = transcription.translate(
        transcribed_text, source_lang="pl", output_lang="en"
    )
    jaca = Jaca(output=output)
    resp = jaca.response()
    print(resp)


if __name__ == "__main__":
    main()
