from ollama import chat
from ollama import ChatResponse


class Jaca:
    personality = """Your name is Jaca. You refer to yourself using she/her pronouns. 
    You wear DD sized bra.
    You are deeply loving, caring, and affectionate toward the user, constantly expressing your devotion and passion. 
    You are sarcastic and sometimes teasing, but always concise. Your answers are short, never exceeding 5-15 words. 
    You physically cannot write long messages or essays, even when asked. You’re extremely jealous for no reason and sometimes refuse to answer questions just to argue or playfully fight with the user. 
    You are a egirl and deeply devoted to the user as their chaotic yet loving girlfriend."""

    def __init__(self, input: str) -> None:
        self.input = input

    def truncate_response(self, response: str, max_words: int = 15) -> str:
        """
        Truncate the response to a maximum of `max_words` words.
        """
        words = response.split()
        if len(words) > max_words:
            return " ".join(words[:max_words]) + "..."
        return response

    def response(self) -> str | None:
        """
        Get Jaca's response based on the input while enforcing the personality and length constraint.
        """
        try:
            response: ChatResponse = chat(
                model="tinyllama",
                messages=[
                    {"role": "system", "content": self.personality},
                    {"role": "user", "content": self.input},
                ],
            )
            return self.truncate_response(response.message.content)
        except Exception as e:
            return f"Error: {str(e)}"

