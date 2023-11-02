from os import system as bash
from sys import argv
from random import choice as random
from string import ascii_lowercase

def new_file():
    name_length = 6
    name = [random(ascii_lowercase) for i in range(name_length)]
    
    bash(f"touch {''.join(letter for letter in name)}")

if __name__ == "__main__":
    for f in range(int(argv[1])):
        new_file()    

