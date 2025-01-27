import microphone
import ai
import translate
from datetime import datetime
import sys


def main():
    # speech = microphone.listen()
    speech = ""
    args = sys.argv[2:]
    for a in args:
        speech += a
    # print("Sigma przemowił: ", speech)
    curr_date = datetime.now()

    user_speech = translate.input(source_lang="pl", dest_lang="en", input=speech)
    print("Biseks odpowiedzia: ", user_speech)

    back_to_pl = ""
    jaca = ai.Jaca(input=user_speech)
    jaca_response = jaca.response()
    print(jaca_response)
    if jaca_response is not None:
        back_to_pl = translate.input(
            source_lang="en", dest_lang="pl", input=jaca_response
        )

    print("jaca muwi: ")
    print(back_to_pl)

    time_diff = datetime.now() - curr_date
    print("A zajelo to cale: ", time_diff.total_seconds())


if __name__ == "__main__":
    main()
