#
# morse.py
#
# ce code traduira l'entrée en morse et inversément
#
#this code will translate any input into morse and back
#
# auteur : 
#   Thibaut Rizzoli (thibaut.rizzoli@hotmail.be)
# 
# Copyright (c) 2020
#

import re
 
#letter = {"a":".-","b"}

def textification(lettre):
    if (lettre == ".- "):
        return("a")
    elif (lettre == "-... "):
        return("b")
    elif (lettre == "-.-. "):
        return("c")
    elif (lettre == "-.. "):
        return("d")
    elif (lettre == ". "):
        return("e")
    elif (lettre == "..-. "):
        return("f")
    elif (lettre == "--. "):
        return("g")
    elif (lettre == ".... "):
        return("h")
    elif (lettre == ".. "):
        return("i")
    elif (lettre == ".--- "):
        return("j")
    elif (lettre == "-.- "):
        return("k")
    elif (lettre == ".-.. "):
        return("l")
    elif (lettre == "-- "):
        return("m")
    elif (lettre == "-. "):
        return("n")
    elif (lettre == "--- "):
        return("o")
    elif (lettre == ".--. "):
        return("p")
    elif (lettre == "--.- "):
        return("q")
    elif (lettre == ".-. "):
        return("r")
    elif (lettre == "... "):
        return("s")
    elif (lettre == "- "):
        return("t")
    elif (lettre == "..- "):
        return("u")
    elif (lettre == "...- "):
        return("v")
    elif (lettre == ".-- "):
        return("w")
    elif (lettre == "-..- "):
        return("x")
    elif (lettre == "-.-- "):
        return("y")
    elif (lettre == "--.. "):
        return("z")
    elif (lettre == ".---- "):
        return("1")
    elif (lettre == "..--- "):
        return("2")
    elif (lettre == "...-- "):
        return("3")
    elif (lettre == "....- "):
        return("4")
    elif (lettre == "..... "):
        return("5")
    elif (lettre == "-.... "):
        return("6")
    elif (lettre == "--... "):
        return("7")
    elif (lettre == "---.. "):
        return("8")
    elif (lettre == "----. "):
        return("9")
    elif (lettre == "----- "):
        return("0")
    elif (lettre == "  "):
        return(" ")
    else:
        return(lettre)

def dico(lettre):
    lettre = lettre.lower()
    if (lettre == "a"):
        return(".- ")
    elif (lettre == "b"):
        return("-... ")
    elif (lettre == "c"):
        return("-.-. ")
    elif (lettre == "d"):
        return("-.. ")
    elif (lettre == "e"):
        return(". ")
    elif (lettre == "f"):
        return("..-. ")
    elif (lettre == "g"):
        return("--. ")
    elif (lettre == "h"):
        return(".... ")
    elif (lettre == "i"):
        return(".. ")
    elif (lettre == "j"):
        return(".--- ")
    elif (lettre == "k"):
        return("-.- ")
    elif (lettre == "l"):
        return(".-.. ")
    elif (lettre == "m"):
        return("-- ")
    elif (lettre == "n"):
        return("-. ")
    elif (lettre == "o"):
        return("--- ")
    elif (lettre == "p"):
        return(".--. ")
    elif (lettre == "q"):
        return("--.- ")
    elif (lettre == "r"):
        return(".-. ")
    elif (lettre == "s"):
        return("... ")
    elif (lettre == "t"):
        return("- ")
    elif (lettre == "u"):
        return("..- ")
    elif (lettre == "v"):
        return("...- ")
    elif (lettre == "w"):
        return(".-- ")
    elif (lettre == "x"):
        return("-..- ")
    elif (lettre == "y"):
        return("-.-- ")
    elif (lettre == "z"):
        return("--.. ")
    elif (lettre == "1"):
        return(".---- ")
    elif (lettre == "2"):
        return("..--- ")
    elif (lettre == "3"):
        return("...-- ")
    elif (lettre == "4"):
        return("....- ")
    elif (lettre == "5"):
        return("..... ")
    elif (lettre == "6"):
        return("-.... ")
    elif (lettre == "7"):
        return("--... ")
    elif (lettre == "8"):
        return("---.. ")
    elif (lettre == "9"):
        return("----. ")
    elif (lettre == "0"):
        return("----- ")
    elif (lettre == " "):
        return("  ")
    else:
        return(lettre)

regexMorse=re.compile(r'''((\.|-|\s)  
(\.|-)*
(\s))''',re.VERBOSE)

#texte vers morse
def trad(Input):
    lettres = []
    morse = []
#isolement de chaque lettre
    for  i in range(len(Input)):
        lettres.append(Input[i])

#traduction lettre par lettre
    for i in range(len(lettres)):
        morse.append(dico(lettres[i]))
#remise sous forme de texte
    output = "".join(morse)
    print (output)

#morse vers texte
def tradInverse(Input):
    lettres = []
    morse = []
    if (Input[-1] != " "):
        Input = Input + " "
#determination du symbole
    for group in regexMorse.findall(Input):
        lettres.append(group[0])
    
#traduction lettre par lettre
    for i in range(len(lettres)):
        morse.append(textification(lettres[i]))
#remise sous forme de texte
    output = "".join(morse)
    print (output)
#récupération du texte
Input = input("veuillez entrer le texte à traduire\n")

#savoir si le code est en morse ou pas
for i in range(len(Input)):
    if (Input[i] == "." or Input[i] == " " or Input[i] == "-"):
        tradInverse(Input)
        break
    else:
        trad(Input)
        break
