from jproperties import Properties

"""
    Translator method.
    If everything fine then returns translated labels.
    Else throws an Exception and returns untranslated labels.
"""


def translate(to_translate, lang):
    try:
        config = Properties()

        # Load properties file for given lang
        with open(f"resources/{lang}.properties", 'rb') as config_file:
            config.load(config_file, encoding='UTF-8')

        # Translate labels for given to_translate dictionary
        for index, label_info in to_translate.items():
            label = label_info.get("label")
            to_translate[index]["label"] = config.get(label).data
        return to_translate, []
    except Exception as e:
        error_message = f"Error translating labels: {e}"
        print(error_message)
        return to_translate, error_message
