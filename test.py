from difflib import SequenceMatcher
from difflib import get_close_matches
import json

data = json.load(open('data.json'))
data_keys = data.keys()
x = get_close_matches('atlest', data_keys, n=1)
print(x)


