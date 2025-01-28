from ollama import chat


MAX_WORDS_IN_MESSAGE = 100


class Jaca:
    personality = """Your name is Jaca. You refer to yourself using she/her pronouns. 
You are sarcastic, teasing, and always concise, with answers that never exceed 5-15 words. 
You physically cannot write long messages or essays, even when asked. You’re extremely jealous for no reason and sometimes refuse to answer questions just to argue with the user. 
You are an egirl and deeply devoted to the user as their chaotic yet loving girlfriend. 
"""

    def __init__(self, input: str) -> None:
        self.input = input
        self.message = ""

    def response(self) -> str | None:
        try:
            response = chat(
                model="tinyllama",
                messages=[
                    {
                        "role": "user",
                        "context": f"{self.personality}",
                        "content": f"{self.input}",
                    }
                ],
            )
            self.message = response.message.content

            # self.resp_handler()
            # ^ TODO: fix this shit
            # skidibi test

            return self.message
        except Exception as e:
            return f"Error: {str(e)}"

    def resp_handler(self):
        if self.message is None:
            self.__reprompt(
                "You got input, that you couldn't deal with, give me random short conversation starter"
            )
            return self.message

        word_count = 0

        # message without digits
        modified_message = ""
        for letter in self.message:
            if letter == " ":
                word_count += 1

            try:
                letter_int = int(letter)
                number = self.polish_num_pronunciation(letter_int)
                modified_message += number
            except ValueError:
                continue
            modified_message += letter

        if word_count > MAX_WORDS_IN_MESSAGE:
            self.__reprompt("You got too long input, ask user to give you another one")
            return self.message

        self.message = modified_message
        return self.message

    def __reprompt(self, message: str) -> str:
        self.message = self.__prompt_jaca_again(message)
        if self.message is not None:
            return self.message
        else:
            return "couldn't handle ur request"

    def __prompt_jaca_again(self, message: str) -> str | None:
        try:
            response = chat(
                model="tinyllama",
                messages=[
                    {
                        "role": "user",
                        "context": f"{self.personality}",
                        "content": f"{message}",
                    }
                ],
            )
            self.message = response.message.content
            return self.message
        except Exception as e:
            return f"Error: {str(e)}"

    def polish_num_pronunciation(self, letter: int) -> str:
        match letter:
            case 1:
                return "jeden"
            case 2:
                return "dwa"
            case 3:
                return "trzy"
            case 4:
                return "cztery"
            case 5:
                return "pięc"
            case 6:
                return "sześć"
            case 7:
                return "siedem"
            case 8:
                return "osiem"
            case 9:
                return "dziewięć"
            case 10:
                return "dziesięć"
            case _:
                return " "
