import ctranslate2
from transformers import AutoTokenizer
import torch
import os
import argostranslate.package
import argostranslate.translate

os.environ["OMP_NUM_THREADS"] = "16"


# pl to en
translator = ctranslate2.Translator("opus-mt-pl-en", device="cpu", compute_type="int8")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pl-en")

# en to pl


# disable gradients during inference to save memory
torch.set_grad_enabled(False)


def input(source_lang: str, dest_lang: str, input: str) -> str:
    if source_lang == "pl" and dest_lang == "en":
        return translate_pl_to_en(input)

    elif source_lang == "en" and dest_lang == "pl":
        return translate_en_to_pl(input)

    else:
        print("invalid language!!!")
        import sys

        sys.exit(1)


def translate_pl_to_en(text: str) -> str:
    tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
    results = translator.translate_batch([tokens])
    target_tokens = results[0].hypotheses[0]
    translated_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(target_tokens))
    return translated_text


def translate_en_to_pl(text: str) -> str:
    input_lang = "en"
    output_lang = "pl"
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == input_lang and x.to_code == output_lang,
            available_packages,
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

    translatedText = argostranslate.translate.translate(text, input_lang, output_lang)

    return translatedText
