"""
morse.py

ce code traduira l'entree en morse et inversement

this code will translate any input into morse and back

auteur :
  Thibaut Rizzoli (thibaut.rizzoli@hotmail.be)

Copyright (c) 2020-2022
"""

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


def alpha_to_morse(atom: str):
    """translate text to morse"""
    temp_morse = []
    atom = atom.lower()
    for i in atom:
        if i in dico:
            temp_morse.append(dico[i])
        else:
            temp_morse.append(i)
    return temp_morse


def morse_to_alpha(mtoa: str):
    """translate morse to text"""
    temp_text = []
    if mtoa[-1] != " ":
        mtoa += " "
    for group in regexMorse.findall(mtoa):
        for key, value in dico.items():
            if value == group[0]:
                temp_text.append(key)
    return temp_text


if __name__ == "__main__":
    MORSE = True
    text = input("texte à traduire:\n")
    for letter in text:
        if letter not in (".", "-", " "):
            MORSE = False
            break
        MORSE = True
    if MORSE is True:

        print("".join(morse_to_alpha(text)))
    else:
        print("".join(alpha_to_morse(text)))
