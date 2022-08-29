#  print('Hello world!')#
#  add more to the print statement, comment and commit the changes you make, then push them to the repo#
print("Would you like to play a game?")
answer = input("Enter yes or no: ")
if answer == "yes":
    # print("What game should we play?: ") --> changed the yes response -J
    print ("Let's have a quiz!")
# what game should we play and how many players can play?

#here is some starter code for a quiz game! Write the next code block-> J

print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

