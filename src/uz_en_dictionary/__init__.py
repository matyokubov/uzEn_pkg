'''
=== Project - [English-Uzbek] Dictionary & Translator ===
Created: 20.11.2021
Author: Matyoqubov Firdavs

Example-1 English-Uzbek:
    from uz_en_dictionary import Translator
    d = Translator(from_lang='en', to='uz')
    print(d.translate("hi"))
    --> int salom!

Example-2 Uzbek-English:
    from uz_en_dictionary import Translator
    d = Translator(from_lang='uz', to='en')
    print(d.translate("bomba"))
    --> (Russian) bomb.

Example-3 Search the words:
    from uz_en_dictionary import Dictionary
    d = Dictionary(lang='en')
    print(d.search("bom"))
    --> {'bomb': ' vt, vi bomba tashlamoq',
         'bombard': ' vt bombardimon etmoq; to`pga tutmoq'}

Example-4 Get words:
    from uz_en_dictionary import Dictionary
    d = Dictionary(lang='uz')
    print(d.getwords_by_letter("q"))
    --> ... (1512 words!)
'''

from .getbase import getword_base
from .dicts import d

class Translator:
    def __init__(self, from_lang, to):
        self.from_lang = from_lang
        self.to = to

    def translate(self, word):
        try:
            base = getword_base(self.from_lang, self.to, word.lower())
            result = base[word.lower()]
            while(result[0] == " "):
                result = result[1:]
            return result
        except:
            return False

class Dictionary:
    def __init__(self, lang):
        self.lang = lang

    def search(self, word):
        return d('s', self.lang, word)

    def getwords_by_letter(self, letter):
        return d('l', self.lang, letter)
