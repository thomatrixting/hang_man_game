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
    words = list(enumerate(words))

    line_choser  = random.randint(1, len(words)) 
    word = "".join([item[1] for item in words if item[0] == line_choser]) #return the word selected
    for a,b in to_replace.items():
        word = word.replace(a,b)
    return "".join(word)

def next_game(word):
    print(f"congratulations the word was {word}")
    user_continue = input("do you want to continue yes(y) or any other leter to exit:") 
    print_estucture() if user_continue == "y" else sys.exit


def print_estucture(word = select_word()):
    leters_said = set()
    word = word
    word_set = set(word)
    while True:
        os.system("clear")
        if leters_said == word_set: next_game(word);break
        print("!adivina la palabra¡")
        print("\n")
        back_slash = "".join(["_" if leter not in leters_said else leter for leter in word])
        print(back_slash)
        user_leter = input("put a leter: ")
        if user_leter in word : leters_said.add(user_leter)

def run():
    print_estucture()


if __name__ == '__main__':
    run()