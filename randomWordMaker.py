#this program makes random words using the alphabet in an array. I haven't done much
#with it yet. created at work out of boredom on July 28th, 2020.

import random # needed to make random choices

sentence = []
ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
VOWELS = ["a","e","i","o","u","y"]
CONSONANTS = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"] 

def again(): # the menu that asks if the user wants to continue
    print("Again? Y/n: ") 
    option = input().lower()
    if(option== "y"):
        main()
    else:
        print("Thank you for using this program.")
        exit(0)
    
def randString(): # makes the random string
    global sentence
    newStr = str("")
    randomNum = random.randint(3,10)
    for i in range(1, randomNum):
        newStr += ALPHABET[random.randint(0,23)]
    sentence.append(newStr)
    print("\nNew word: ",newStr,"\n")
    print("Sentence so far: ",' '.join(sentence),"\n")

def getInput(): # get input from user
    option = input("Please select an option from the list: ")
    return option

def listOptions(): # list the choices for the user
    print("Welcome to the random word/sentence maker version 0.1!-\nOptions: \n1. Print a random string.\n")
    option = getInput()
    if(option == "1"):
        randString()
    elif(option == "2"):
        print("Option is Two.")
    else:
        print("Option is Invalid.")
        exit(0)

def main(): # run the program
    listOptions()
    again()

main() # run main
