import json
from difflib import get_close_matches

data = json.load(open('data.json'))
data_keys = data.keys()


def translate(word_param):
    """A function that return the specific word meaning"""
    if word_param in data:
        return data[word_param]

    elif word_param.upper() in data_keys:
        return data[word_param.upper()]
    elif get_close_matches(word_param, data_keys, n=1) is not None:
        a = input(f'Did you mean {get_close_matches(word_param, data_keys)[0]} instead? if you did enter Y '
                  f'otherwise enter N: ')
        if a.lower() == 'y':
            new_param = get_close_matches(word_param, data_keys)[0]
            return data[new_param]
        else:
            return 'Please double check your word!'
    else:
        return 'Please double check your word!'


word = input('Enter word: ')
translated = translate(word.lower())
if type(translated) == list:
    for item in translated:
        print(item)
else:
    print(translated)
