import json
import difflib
import random
from difflib import get_close_matches
from random import randint

data = json.load(open('data.json'))


def meaning_of(word):
    #Accepts 'word' and returns a meaning from data.json

    if word in data:
        return data[word] 
    elif len(get_close_matches(word, data.keys())) > 0:
        
        #get_close_match(key, list) returns a list of close matches
        prompt = input("Did you mean %s instead? Enter Y if yes, or N if not.\n> " % get_close_matches(word, data.keys())[0])
        prompt = prompt.upper()
        
        if prompt == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif prompt == 'N':
            return "Word not found"
        else:
            return "Invalid entry"           
    else:
        return "Word not found"


word =  input('[ENTER WORD]: ').lower()

while word != "":

    output = meaning_of(word)

    if type(output) == list:
        
        for item in output:
            print(item)
    else:
        print(output)   
    
    word =  input('\nPress [ENTER] to EXIT\n[ENTER WORD]:').lower() 