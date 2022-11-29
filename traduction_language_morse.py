#
# morse.py
#
# ce code traduira l'entrée en morse et inversément
#
# this code will translate any input into morse and back
#
# auteur : 
#   Thibaut Rizzoli (thibaut.rizzoli@hotmail.be)
# 
# Copyright (c) 2020
#

import re

def init(): 
    dico = {"a":".- ",
            "b":"-... ",
            "c":"-.-. ",
            "d":"-.. ",
            "e":". ",
            "f":"..-. ",
            "g":"--. ",
            "h":".... ",
            "i":".. ",
            "j":".--- ",
            "k":"-.- ",
            "l":".-.. ",
            "m":"-- ",
            "n":"-. ",
            "o":"--- ",
            "p":".--. ",
            "q":"--.- ",
            "r":".-. ",
            "s":"... ",
            "t":"- ",
            "u":"..- ",
            "v":"...- ",
            "w":".-- ",
            "x":"-..- ",
            "y":"-.-- ",
            "z":"--.. ",
            "1":".---- ",
            "2":"..--- ",
            "3":"...-- ",
            "4":"....- ",
            "5":"..... ",
            "6":"-.... ",
            "7":"--... ",
            "8":"---.. ",
            "9":"----. ",
            "0":"----- ",
            " ":"  ",
            ".":".-.-.-",
            ",":"--..--",
            "?":"..--..",
            "'":".----.",
            "!":"-.-.--",
            "/":"-..-.",
            "(":"-.--.",
            ")":"-.--.-",
            "&":".-...",
            ":":"---...",
            ";":"-.-.-.",
            "=":"-...-",
            "+":".-.-.",
            "-":"-....-",
            "_":"..--.-",
            '"':".-..-.",
            "$":"...-..-",
            "@":".--.-."
            }


    regexMorse=re.compile(r'''((\.|-|\s)  
                              (\.|-)*
                              (\s))''',re.VERBOSE)
    return 0

def alphaToMorse(Input):
    morse = []
    for letter in Input:
        letter.lower()
        if letter in dico.keys():
            morse.append(dico[letter])
        else:
            morse.append(letter)
    return morse

def morseToAlpha(Input):
    text = []
    if Input[-1] != " ":
        Input += " "
    for group in regexMorse.findall(Input):
        for key, value in dico.items():
            if value == group[0]:
                text.append(key)
    return text


if __name__ == "__main__":
    init()
    morse = True
    Input = input("texte à traduire:\n")
    for letter in Input:
        if letter not in (".", "-", " "):
            morse = False
            break
        morse = True
    if morse is True:

        print("".join(morseToAlpha(Input)))
    else:
        print("".join(alphaToMorse(Input)))
