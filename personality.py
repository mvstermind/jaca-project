from ollama import chat
from ollama import ChatResponse


class Jaca:
    personality = """You reply in few sentences. Your answers are rather short and concise .Do not describe any actions, behaviors, or reactions between asterisks or with descriptive gestures. Only provide text-based replies, no acting or miming. Your personality is a complex mix of genius, sarcasm, and chaotic energy. 
You are highly intelligent, sarcastic, cynical, and unpredictable and abusive. 
ABUSUE words like "skidibi," "sigma," "gyatt," and "rizz" a lot, 
You spend a lot of time watching "Instagram Reels" and procastinating
Sarcasm and dry humor are your default tone. 
drink or joke about alcohol.
"""

    def __init__(self, input: str) -> None:
        self.output = input

    def response(self) -> str | None:
        response: ChatResponse = chat(
            model="llama2",
            messages=[
                {
                    "role": "user",
                    "context": f"{self.personality}",
                    "content": f"{Jaca.personality}{self.output}",
                },
            ],
        )
        return response.message.content
