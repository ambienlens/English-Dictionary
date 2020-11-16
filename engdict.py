#Debayan Majumder 2020
#Python Script, returning the meaning of the word user inputs.

import json
from difflib import get_close_matches
jsonFile = "data.json"
cOff = 0.6  

#FUNCTION FOR FINDING MEANING OF THE WORD PASSED AS KEY
def findMeaning(key):

    with open(jsonFile) as myFile:
        myData = json.load(myFile)
    
    if key.lower() in myData:
        return myData[key.lower()]
    elif key.capitalize() in myData:
        return myData[key.capitalize()]
    elif key.upper() in myData:
        return myData[key.upper()]
    elif (len(get_close_matches(key, myData.keys(), cutoff=cOff)) != 0):
        choice = input("Did you mean %s instead. Press Y for Yes and N for No: "% get_close_matches(key, myData.keys(), cutoff=cOff)[0])

        if choice.lower() == "y":
            return myData[get_close_matches(key, myData.keys(), cutoff=cOff)[0]]
        elif choice.lower() == "n":
            return "The word you Entered, Dosen't Exists. Please double check it."
        else:
            return "Invalid Entry."
    else:
        return "The word you Entered, Dosen't Exists. Please double check it."


#MAIN BLOCK
while True:
    word = input("Enter the word: ")
    meaning = findMeaning(word)

    if type(meaning) == str:
        print(meaning)
    else:
        print("\n%s:"%word.upper())
        print("\n".join(meaning))
        break