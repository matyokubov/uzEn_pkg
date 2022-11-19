from .database.controller import read

def getword_base(fl, tl, w):
    if(str(type(w)) == "<class 'str'>"):
        first_letter = w[0].lower()
        base_folder = f"{fl}-{tl}"
        return read(base_folder, first_letter)
    else:
        return False
