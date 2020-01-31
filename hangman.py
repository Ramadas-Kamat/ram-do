# Hangman game

import random

POOL={"BENGALURU":"The city also known as the IT capital of India",
      "VIAGRA":"Every intercourse is incomplete without me",
      "CATASTROPHE":"This is a synonym of Disaster",
      "LINDANE":"Another name of Gammaxene"}
     
WORDS=["BENGALURU","VIAGRA","CATASTROPHE","LINDANE"]

HANGMAN = (
            """
            ------
            | |
            |
            |
            |
            |
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |
            |
            |
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |/
            |
            |
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |/ \
            |
            |
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |/|\
            | | 
            |
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |/|\
            | | 
            |/
            |
            |
            |
            ----------
            """,
            """
            ------
            | |
            | O
            |/|\
            | | 
            |/ \
            |
            |
            |
            ----------
            """
            )

word=random.choice(WORDS)
max=len(HANGMAN)-1
n=0


print("\nWelcome to the HANGMAN game\n")
print("\n\n",HANGMAN[0])

guessed=[]
scratch="-"*len(word)

print("Your hint is: \t",POOL[word])


while n<max and  scratch!=word :
    
    ch=input("\nMake a  guess\t")
    ch=ch.upper()

    while ch in guessed:
        print(ch," is already guessed\n")
        ch=input("\nMake a  guess\t")
        ch=ch.upper()
        
    guessed.append(ch)
    
    if ch in word :
        print("You guessed it right\n")
        
        new=""
        i=0
        for i in range(len(word)) :
            if ch==word[i] :
                new+=ch
                
            else:
                new+=scratch[i]


        scratch=new
        
    else:
        print("Oops the word",ch,"is not present")
        n+=1
        print("\n\n",HANGMAN[n])
    if scratch!=word:
        print("Words used:\t",guessed)
        print("\nSo far the word is: ",scratch)
        
if n==max:
    print("\n\n",HANGMAN[n])
    print("\nYou have been hanged\n")
else:
    print("\nYou got the word")

print("The word is:\t",word)



