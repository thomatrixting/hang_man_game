import os
import time
import random
from functools import reduce

def run():
    def select_word():
        to_replace = {"Ã³":"o", "Ã±": "ñ", "Ã©" : "e", "Ã":"i" }
        with open("Words.txt","r",encoding="utf-8") as file:
            words = [line for line in file.readlines()]
            words = list(map(lambda word : word.strip(),words)) # remove the \n
            words = list(enumerate(words)) #enumerate the words s

        line_choser  = random.randint(1, words[-1][0]+1) 
        word = "".join([item[1] for item in words if item[0] == line_choser]) #return the word wer
        for a,b in to_replace.items():
            word = word.replace(a,b)
        return "".join(word)
            
    print(select_word())


    #lambda leter_said,leter: leter if leter in leter_said else "_"


if __name__ == '__main__':
    run()