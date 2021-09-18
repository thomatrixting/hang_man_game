import os
# import time
import random
import sys
# from functools import reduce

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

def next_game(word):
    print(f"congratulations the word was {word}")
    user_continue = input("do you want to continue yes(y) or any other leter to exit:") 
    print_estucture() if user_continue == "y" else sys.exit


def print_estucture(word = select_word()):
    leter_said = []
    while True:
        os.system("clear")
        if sum([letra in leter_said for letra in word]) == len(word): next_game(word)
        print("!adivina la palabra¡")
        print("\n")
        back_slash = "".join(["_" if leter not in leter_said else leter for leter in word])
        print(back_slash)
        user_leter = input("put a leter: ")
        leter_said.append(user_leter)

def run():
    print_estucture()


if __name__ == '__main__':
    run()