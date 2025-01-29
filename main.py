import microphone
import ai
import local_tts
import translate
from datetime import datetime
import os
import sys


def main():
    while True:
        # speech = microphone.listen()
        # print("Powiedziałeś: ", speech)
        speech = input("WPISUJ: ")

        curr_date = datetime.now()
        user_speech = translate.input(source_lang="pl", dest_lang="en", input=speech)
        print("Tłumaczenie na ang: ", user_speech)

        ai_resp_pol = ""
        jaca = ai.Jaca(input=user_speech)
        jaca_response = jaca.response()
        print(jaca_response)

        if jaca_response is not None:
            ai_resp_pol = translate.input(
                source_lang="en", dest_lang="pl", input=jaca_response
            )
        print("Odpowiedź bota: ", ai_resp_pol)

        time_diff = datetime.now() - curr_date
        print("A zajelo to cale: ", time_diff.total_seconds())
        print("\n\ntts na beacie")
        # local_tts.read(ai_resp_pol)


if __name__ == "__main__":
    main()
