from google.cloud import translate_v2 as translate


def validate_msg_in_lang(message: str, lang: str):
    translator = translate.Client()
    result = translator.translate(message, target_language='en')
    return result["detectedSourceLanguage"] == lang
