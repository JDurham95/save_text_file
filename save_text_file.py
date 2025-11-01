#Microservice #2 - save_text_file
#CS 361 Fall 2025 Team 30
#Gino Febles Castillo, Kevin Frias, Gabriel-Jean Bertrand, Jacob Durham, Justin Holley

import os

def save_text_file(file):
    """
    The user will pass a text file. The first line of the file indicates either append ("a") or write ("w").
    The second line of the file is the text to be saved. The third line of the file is the name to be saved
    """
    with open(file, "r") as f:
        content = f.readlines()
    action = content[0]
    if content[2]:
        name = content[2]
    else:
        name = "temp.txt"

    if action == "a" and os.path.exists(name):
        with open(name, "a", encoding="utf-8") as f:
            f.write(content[1])
    else:
        with open(name, "w", encoding="utf-8") as f:
            f.write(content[1])

