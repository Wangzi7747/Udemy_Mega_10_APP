import json
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data, cutoff=0.8)) > 0:
        yn = input(
            f'Do you mean { get_close_matches(word, data, cutoff=0.8)[0]}, please enter Y!')
        if yn == "Y":
            new_word = get_close_matches(word, data, cutoff=0.8)[0]
            return data[new_word]
        else:
            return "The word does not exist.Please double check!"
    else:
        return "The word does not exist.Please double check!"


word = input("Enter Word:")
output = translate(word)
for item in output:
    print(item)
