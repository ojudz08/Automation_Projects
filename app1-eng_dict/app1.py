import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    w_match = get_close_matches(w, data.keys())
    if w in data:
        return data[w.lower()]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(w_match) > 0:
        yn = input(f"Did you mean {w_match[0]} instead? Enter Y if yes, or N if no: " )
        if Yes_No(yn) == "Y":
            return data[w_match[0]]
        elif Yes_No(yn) == "N":
            return "Word doesn't exist, check again."
    else:
        return "Word doesn't exist. Please double check it."


def Yes_No(yn):
    if (yn == "Y" or yn == "N") == True:
        return yn
    else:
        yn = input("Kindly input Y if yes, N if no: ")
        return yn

    

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)