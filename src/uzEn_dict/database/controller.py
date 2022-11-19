import json
import os

def read(folder, word_letter):
    base = json.load(open(f"{os.getcwd()}/uz_en_dictionary/database/{folder}/{word_letter}.json"))
    return base
