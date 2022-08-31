#  print('Hello world!')#
#  add more to the print statement, comment and commit the changes you make, then push them to the repo#
import re

print("                 Would you like to play a game?")
answer = input("Enter yes or no: \n")
if answer == "yes":
    # print("What game should we play?: ") --> changed the yes response -J
    print ("                    Let's have a quiz!")
# what game should we play and how many players can play?

#here is some starter code for a quiz game! Write the next code block-> J

print('                 Welcome to AskPython Quiz\n')
answer=input('Are you ready to play the Quiz ? (yes/no) : \n')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input("\nQuestion 1: What is your Favourite programming language?"'\n')
    answer=input("\nQuestion 2: A Dutch programmer by the name Guido van Rossum created which programming language?" '\n')
    answer=input("\nQuestion 3: In Savvy Coder's Data Analytics program, we are required to use this programming language when handling large Datasets:  "'\n')
    if answer.lower()=='python':
        score += 1
        print('\nCorrect! Congratulations on completing the AskPython Quiz')
        
    else:
        print('Wrong Answer :(')
        



