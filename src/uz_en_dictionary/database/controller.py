import json
import os

def read(folder, word_letter):
    pkgPath = __file__.split("\\")[:-1]
    pkgPath = "\\".join(pkgPath)
    base = json.load(open(f"{pkgPath}\{folder}\{word_letter}.json"))
    return base
