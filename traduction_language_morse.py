#
# morse.py
#
# ce code traduira l'entree en morse et inversement
#
# this code will translate any input into morse and back
#
# auteur : 
#   Thibaut Rizzoli (thibaut.rizzoli@hotmail.be)
# 
# Copyright (c) 2020
#

import re

dico = {
        "a":".- ","b":"-... ","c":"-.-. ",
        "d":"-.. ","e":". ","f":"..-. ",
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

regexMorse = re.compile(r'''((\.|-|\s)(\.|-)*(\s))''',re.VERBOSE)


"""translate text to morse"""
def alphaToMorse(Input:str):
    morse = []
    for letter in Input:
        letter.lower()
        if letter in dico.keys():
            morse.append(dico[letter])
        else:
            morse.append(letter)
    return morse

"""translate morse to text"""
def morseToAlpha(Input:str):
    text = []
    if Input[-1] != " ":
        Input += " "
    for group in regexMorse.findall(Input):
        for key, value in dico.items():
            if value == group[0]:
                text.append(key)
    return text


if __name__ == "__main__":
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
