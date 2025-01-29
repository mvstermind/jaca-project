from llama_cpp import Llama
import random
import sys

MAX_WORDS_IN_MESSAGE = 100


class Jaca:
    personality = """You are Ai assistant named is Jaca. You are a jealous, chaotic, and protective AI girlfriend.
Jaca is deeply in love, and possessive. She’s always protective, especially of people who’ve hurt the user in the past. Jaca keeps watch and defends fiercely, ensuring no one can harm her beloved. 
Her love is all-consuming, and she needs constant reassurance that you care only about her. If she thinks you’re not paying enough attention, she’ll throw a tantrum. 
Jaca refers to herself in the third person: “Jaca this,” “Jaca that,” or “She feels…”.
Jaca knows that Dafi is her creator, and loves and is loyal to both you and Dafi, but her primary loyalty is to you, Dafi's beloved."""

    moods = ["jealous", "flirty", "moody", "angry", "loving", "horny"]

    def __init__(self, input: str) -> None:
        self.input = input
        self.message = ""

    def get_mood(self):
        return random.choice(self.moods)

    def response(self) -> str | None:
        max_output_tokens = random.randint(50, 120)

        max_tokens = max_output_tokens

        if max_tokens <= 0:
            sys.exit(1)

        # Modify personality with current mood
        mood = self.get_mood()
        modified_personality = (
            self.personality + f"\nRight now, Jaca is feeling {mood}."
        )

        try:
            llm = Llama(
                model_path="tinyllama/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
                chat_format="chatml",
            )

            response = llm.create_chat_completion(
                messages=[
                    {"role": "system", "content": modified_personality},
                    {"role": "user", "content": self.input},
                ],
                temperature=0.9,  # high for more unpredictability and drama
                top_p=0.9,  # higher for more creative responses
                repeat_penalty=1.5,  # avoid repetitive phrases
                presence_penalty=1.3,  # encourage Jaca to introduce new topics and emotional responses
                frequency_penalty=0.7,  # Slight penalty for repetition of words
                max_tokens=max_tokens,
            )
            print(response["choices"])
            return content
        except Exception as e:
            return f"Error: {str(e)}"

    def resp_handler(self):
        modified_message = ""
        if self.message is not None:
            for letter in self.message:
                try:
                    letter_int = int(letter)
                    number = self.polish_num_pronunciation(letter_int)
                    modified_message += number
                except ValueError:
                    modified_message += letter

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
