import os
import time
import random
from functools import reduce

def run():
    def select_word():
        with open("Words.txt","r",encoding="utf-8") as file:
            words = [line for line in file.readlines()]
            words = list(map(lambda word : word.strip(),words)) # remove the \n
            words = list(enumerate(words))
            print(words)
        with open("Words.txt","r",encoding="utf-8") as file:
            N_lines =  reduce(lambda a, b: a + b,[1 for line in file])
            line_choser  = random.randint(1, N_lines+1)
            return [item[1] for item in words if item[0] == line_choser]
            

    print(select_word())





if __name__ == '__main__':
    run()