import os
import time
import random
from functools import reduce

def run():
    def select_word():
        adjusted_word = {"Ã³":"o", "Ã±": "ñ", "Ã©" : "e", "Ã":"i" }
        with open("Words.txt","r",encoding="utf-8") as file:
            words = [line for line in file.readlines()]
            words = list(map(lambda word : word.strip(),words)) # remove the \n
            words = list(enumerate(words)) #enumerate the words s
        with open("Words.txt","r",encoding="utf-8") as file:
            N_lines =  reduce(lambda a, b: a + b,[1 for line in file])
            line_choser  = random.randint(1, N_lines+1)
        word = ([item[1] for item in words if item[0] == line_choser]) #return the word wer
        word = list(map(lambda leter: adjusted_word[leter] if leter in adjusted_word.keys() else leter,word)) #change the wrong leters

        return "".join(word)
            

    print(select_word())





if __name__ == '__main__':
    run()