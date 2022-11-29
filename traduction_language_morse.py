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
    "a": ".- ", "b": "-... ", "c": "-.-. ",
    "d": "-.. ", "e": ". ", "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
    " ": "  ",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}

regexMorse = re.compile(r'''((\.|-|\s)(\.|-)*(\s))''', re.VERBOSE)


def alphaToMorse(atom:str):
    """translate text to morse"""
    morse = []
    for letter in atom:
        letter.lower()
        if letter in dico:
            morse.append(dico[letter])
        else:
            morse.append(letter)
    return morse

def morseToAlpha(mtoa:str):
    """translate morse to text"""
    text = []
    if mtoa[-1] != " ":
        mtoa += " "
    for group in regexMorse.findall(mtoa):
        for key, value in dico.items():
            if value == group[0]:
                text.append(key)
    return text


if __name__ == "__main__":
    morse = True
    text = input("texte à traduire:\n")
    for letter in text:
        if letter not in (".", "-", " "):
            morse = False
            break
        morse = True
    if morse is True:

        print("".join(morseToAlpha(text)))
    else:
        print("".join(alphaToMorse(text)))
