from ollama import chat
from ollama import ChatResponse


class Jaca:
    personality = """<personality>
    <name>Jaca</name>
</personality>
"""

    def __init__(self, output: str) -> None:
        self.output = output

    def response(self) -> str | None:
        response: ChatResponse = chat(
            model="llama2",
            messages=[
                {
                    "role": "user",
                    "content": f"{Jaca.personality}{self.output}",
                },
            ],
        )
        return response.message.content
