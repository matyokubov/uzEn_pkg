from .database.controller import read
neg = {"uz": "en", "en": "uz"}

def d(m, lang, inp):
    if(str(type(inp)) == "<class 'str'>"):
        try:
            if(m == "s"):
                global neg
                base = f"{lang}-{neg[lang]}"
                json = read(base, inp[0])
                result = {}
                for word in json.keys():
                    if(inp in word):
                        result[word] = json[word]
                return result
            elif(m == "l"):
                base = f"{lang}-{neg[lang]}"
                json = read(base, inp[0])
                return json
            else:
                return False
        except:
            return False
    else:
        return False
