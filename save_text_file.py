#Microservice #2 - save_text_file
#CS 361 Fall 2025 Team 30
#Gino Febles Castillo, Kevin Frias, Gabriel-Jean Bertrand, Jacob Durham, Justin Holley

import os

def save_text_file(file):
    """
    The user will pass a text file. The first line of the file indicates either append ("a") or write ("w").
    The second line of the file is the text to be saved. The third line of the file is the name to be saved
    """

    #open the file, get the individual lines as the content array. clear the contents of the passed in file.
    with open(file, "r") as f:
        content = f.readlines()
    open(file, "w").close()

    #the first line is action to be taken, either append or write
    action = content[0]

    #the third line is the name of the file
    if content[2]:
        name = content[2]

        #append ".txt" if needed
        if name[-4:] != ".txt":
            name = name + ".txt"
    else:
        name = "temp.txt"

    #append if the action is "a" and the name already exists, otherwise write
    if action == "a" and os.path.exists(name):
        with open(name, "a", encoding="utf-8") as f:
            f.write(content[1])
    else:
        with open(name, "w", encoding="utf-8") as f:
            f.write(content[1])

