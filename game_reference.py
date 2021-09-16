import os
import time

def print_structure(leters_said = [], word= "cafe"):
        os.system("cls")
        print("!adivina la palabra¡")
        print("\n")
        for leter in word:
            back_slash = (lambda leter,leters_said : leter if leter in leters_said else "_") #put or not the back slash
            print(back_slash(leter,leters_said),end="")

        print("\n")

def end(word):
    print(f"gracias por jugar la palabra era {word}")

def game(leters_said,word):
    word_list = [i for i in word]
    print_structure(leters_said,word)
    end(word) if [i for i in word_list] else None
    leter_imput = input("pon la letra: ") #problem of loop
    if leter_imput not in leters_said:
        leters_said.append(leter_imput)

    elif leter_imput in leters_said:
        print("ya has puesto esa letra")
        time.sleep(5)

    else:
        print(f"unknow error/ info[ imput:{leter_imput} leter said{leters_said} ]")   

    game(leters_said,word)   


def run():
    word_ = "cafe"
    leters_said_ = []
    game(leters_said_,word_)

    
    

if __name__ == '__main__':
    run()