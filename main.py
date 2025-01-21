from audio import transcription
from ollama import chat
from ollama import ChatResponse
from personality import Jaca


def main():
    transcribed_text = transcription.audio_from_mic()
    output = transcription.translate(
        transcribed_text, source_lang="pl", output_lang="en"
    )
    print(output)
    response: ChatResponse = chat(
        model="llama2",
        messages=[
            {
                "role": "user",
                "content": f"{Jaca.personality}{output}",
            },
        ],
    )
    print(response.message.content)


if __name__ == "__main__":
    main()
