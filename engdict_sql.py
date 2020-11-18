#DEBAYAN MAJUMDER 2020
#Verion 1.0
#This is a python script, which returns the meaning of a word entered by the User.
#This python script makes use of mySQL database.
#N.B: THIS SCRIPT HAS A LOT OF TIME COMPLEXITY AND IT TAKES TOO MUCH TIME TO SEARCH
#     REQUIRED DATA FROM THE DATABASE. YOU CAN USE THIS SCRIPT BUT IT WON'T DO ANY
#     GOOD TO YOUR PROGRAM. 

import mysql.connector
from difflib import get_close_matches
sqlstr = "SELECT * FROM Dictionary WHERE"
cOff = 0.6

def SQLSearch(obj, key):
    con = mysql.connector.connect(
        user = "ardit700_student", 
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
    )
    cursor = con.cursor()
    query = cursor.execute("SELECT %s FROM Dictionary %s"%(obj, key))
    result = cursor.fetchall()

    return result

def convertToList(list):
    newList = []
    for i in range(len(list)):
        newList.append(list[i][0])

    return newList

def Meaning(word):
    Search = "WHERE Expression = '%s'"%word
    obj = "*"
    if len(SQLSearch(obj, Search)) != 0:
        return SQLSearch(obj, Search)
    elif len(SQLSearch(obj, Search)) == 0:
        newWord = get_close_matches(word, convertToList(SQLSearch("Expression", "")))[0]
        choice = input("Did you mean %s instead? Press Y for Yes and N for No: "%newWord)
        if(choice.lower() == "y"):
            return SQLSearch("*", "WHERE Expression = '%s'"%newWord)
        elif(choice.lower() == "n"):
            return "Sorry We Didnt Understand!"
        else:
            return "Wrong Credentials"

#MAIN BLOCK
word = input("Enter the word: ")
meaning = Meaning(word)

print("%s:"%meaning[0][0].upper())
for this in range(len(meaning)):
    print(meaning[this][1])