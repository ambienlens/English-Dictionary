#Debayan Majumder 2020
#Verion 1.0
#This is a python script, which returns the meaning of a word entered by the User.

#importing std. libraries
import json
from difflib import get_close_matches

#The jsonFile location and the cutoff percentage
jsonFile = "data.json"
cOff = 0.6  

#FUNCTION FOR FINDING MEANING OF THE WORD PASSED AS KEY
def findMeaning(key):
    
    #opening the .json file and storing the information as <dict> in a variable
    with open(jsonFile) as myFile:
        myData = json.load(myFile)
    
    #checking for the matches. 
    #First, checking with the entered word in lowercase, uppercase and only first character uppercase
    #Then, looking for close matches and promting the user a guessed word, and returning the output
    #of the word if the user agrees with the guessed word
    #IMP: THE FUNCTION RETURNS A TUPLE OF THE WORD AND THE MEAINING OF THE WORD
    if key.lower() in myData:
        return (key, myData[key.lower()])
    elif key.capitalize() in myData:
        return (key, myData[key.capitalize()])
    elif key.upper() in myData:
        return (key, myData[key.upper()])
    elif (len(get_close_matches(key, myData.keys(), cutoff=cOff)) != 0):

        #Checking if the close match produces an empty list, which means there are no close matches.
        choice = input("Did you mean %s instead. Press Y for Yes and N for No: "% get_close_matches(key, myData.keys(), cutoff=cOff)[0])
        newWord = get_close_matches(key, myData.keys(), cutoff=cOff)[0]

        if choice.lower() == "y":
            return (newWord, myData[newWord])
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

    #Checking for return type and printing them in their respective order.
    if type(meaning) == str:
        print(meaning)
    else:
        print("\n%s:"%meaning[0].upper())
        print("\n".join(meaning[1]))
        break
