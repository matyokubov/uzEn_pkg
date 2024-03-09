# UZ-EN Dictionary

UZ-EN Dictionary is a Python library to translate words (uz-en; en-uz).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install uz_en_dictionary.

```bash
pip install uz-en-dictionary
```

## Usage

```python
from uz_en_dictionary import Translator
d = Translator(from_lang='en', to='uz') # EN-UZ
print(d.translate("believe"))
# vt, vi 1) ishonmoq; 2) imon keltirmoq; 3) o`ylamoq
```
```python
from uz_en_dictionary import Translator
d = Translator(from_lang='uz', to='en') # UZ-EN
print(d.translate("maqsad"))
# (Arabic) intent, purpose, aim. ~ida for the purpose of, in order to.
```
```python
from uz_en_dictionary import Dictionary
d = Dictionary(lang='en')
print(d.search("gramm")) # Search mode
# {'grammar': ' n [U] grammatika', 'grammatical': ' adj. grammatikaga oid','gramme': ' n [C] misqol, gram'}
```
```python
from uz_en_dictionary import Dictionary
d = Dictionary(lang='uz')
print(d.getwords_by_letter("q")) # Get words from letter
# <Words (q)>
```
