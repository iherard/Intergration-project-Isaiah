#Name - Isaiah Herard
#Program Descripition: Basic puzzle game
#https://stackoverflow.com/questions/40792830/yes-or-no-output-in-python
#https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
#https://iqcode.com/code/python/how-to-ask-a-yes-or-no-question-on-python#:~:text=how%20to%20ask%20a%20yes%20or%20no%20question,that.%20else%3A%20print%20%28%22Please%20enter%20yes%20or%20no.%22%29
#https://www.w3schools.com/python/gloss_python_if_or.asp
#https://www.hackerrank.com/contests/1500f22/challenges/3-booleans
print(("Welcome to Power Frenzy"))
print("\nType one to continue\n For unused programming/extra one of the following: S.E, N.O.E, M.S.C, A.S.C, Range, Not, Or:")
# Input lets the user put in what response they want to put in
answer = input()
# If Help put certain inputs lead to a certain output. Source:yes or no output, stackoverflow and igcode
if answer == 'one':
    print("Lets start with a tutorial")
# elif mean else if meaning that if user puts a different certain input will lead them to another output
# Also a string is used here
# S.E-String Example
elif answer == 'S.E':
    print("type name:")
    name = input()
    print("Hello", name)
    print("Restart the program")
# basically gives out the basic function of calculating numbers, the % put the remainder and the  exponents(**).
# N.O.E-Numeric Operators Examples
elif answer == 'N.O.E':
    print("5*5=", 5 * 5, sep='')
    print("5-5=", 5 - 5, sep='')
    print("5/5=", 5 / 5, sep='')
    print("5+5=", 5 + 5, sep='')
    print("5**5=", 5 ** 5, sep='')
    print("5%2=", 5 % 2, sep='')
    print("Restart the program")
# use as a string to add or multiply numbers/M.S.C-Multipling string calculation/user can enter a number
elif answer == 'M.S.C':
    print("num1=")
    num1 = int(input())
    print("num2=")
    num2 = int(input())
    totalMult = int(num1 * num2)
    print("num1*num2=", totalMult)
    print("Restart the program")
# add the two numbers that you type in to add up the total/ user can enter in numbers
elif answer == 'A.S.C':
    print("num1=")
    num1 = int(input())
    print("num2=")
    num2 = int(input())
    totalAdd = int(num1 + num2)
    print("num1+num2=", totalAdd)
    print("Restart the program")
#Basically determines the range of the function and see if it is within it.  But in this case, less or Big
elif answer == "Range":
    number = int(input("Type a number that is less than or more than 5"))
    if number < 5:
        print("Less")
    elif number <= 5:
        print("Equal, restart program")
    else:
        print("Big")
#Either answer is correct 
elif answer == "Or":
    x = int(input("Enter Numbers"))
    y = int(input("Enter Numbers"))
    if x < y or y < x:
        print("Correct")
        print("Restart program")
#Not function basically makes the results is reverse
elif answer == "Not":
    print(2 < 1)
    number = 2
    print(not(number > 1))
    print("Restart program")
else:
    print("GAME OVER \n Next time, STICK WITH PROGRAM, or you wll Crash.")
#And statements
    weight = float(input("Enter weight "))
    cost = float(input("Enter cost "))
    print((weight < 10) and (cost <= 20))
if answer == 'one':
    def messageTwo(sting):
        for tutorial in "Tutorial \nWithin this game, you need to pick the right weapons or powerups to continue. ":
            print(tutorial, end="")
    if __name__ == '__main__':
        msgTwo = "Within this game, you need to pick the right weapons or powerups to continue.  "
        messageTwo(msgTwo)
    def tutorialcont(sting):
        for tutorialcont in "\nYou have options between  Drills, swords, and gauntlets.":
            print(tutorialcont, end="")
    if __name__ == '__main__':
        tutcont = "\nYou have options between  Drills, swords, and gauntlets."
        tutorialcont(tutcont)
    def tutorialcontTwo(sting):
        for tutorialcontTwo in "Here is which weapon can break what obstacle:\nDrill-Swirling Wall\nGaunlets-Metal Wall\nSwords-Metal Polls":
            print(tutorialcontTwo, end="")
    if __name__ == '__main__':
        tutcontTwo = "\nYou have options between  Drills, swords, and gauntlets."
        tutorialcontTwo(tutcontTwo)
    print("Practice one \nNow As you are walking foward there is a swirling wall\n Select thy weapon:")
    print("a.Drill\nb.GAUNTLET\nc.sword")
def messageThree(sting):
    for PracticeOne in "a.Drill\nb.GAUNTLET\nc.sword":
        print(PracticeOne, end="")
    if __name__ == '__main__':
        msgThree = "PA", "AAAAAAAWER DRILLLLLLLL"
        messageThree(msgthree)
answer = input()
if answer == "a":
    # "PO" * 3 prints po three times
    print("PO" * 3, "OOOOOWER DRILLLLLLLL ACTIVATED", sep='')
    print("zzRTTTTTTTTTTTT!")
    print("YOU HAVE MADE THROUGH LEVEL ONE")
else:
    print("Life Bar:", 3 - 1, "\noh sorry, forgot to mention, you get three lives in this game.You can regain a life")
    print("back if You answer the next one correctly. Now, lets see if you survive the next obstacle")
print("Practice two: \nThere is a metal wall in your way:\nSelect thy weapon:\na.Drill\nb.GAUNTLET\nc.sword")
def messageFour(msgFour):
    for PracticeTwo in "a.Drill\nb.GAUNTLET\nc.sword":
        print(PracticeTwo, end="")
    if __name__ == '__main__':
        msgFour = "DRAGON GAUNLETS ENGAGED \nROOOOOAAAAAAAAAAAAAARRRRRRRRRRRR"
        messageFour(msgFour)
answer = input()
if answer == "b":
    print("Life Bar:3")
    print("DRAGON GAUNLETS ENGAGED \nROOOOOAAAAAAAAAAAAAARRRRRRRRRRRR POW POW")
else:
    print("Life bar:", 2 - 1, "\n thats ok, lets try the next question")
    print(
        "The last challenge, Metal Polls blocks the way, and since this the last challenge,wrong answer is instant death")
    print("\nSelect thy weapon:")
    print("a.Drill\nb.GAUNTLET\nc.sword")
def messageFive(sting):
    for PracticeThree in "a.Drill\nb.GAUNTLET\nc.sword":
        print(PracticeThree, end="")
    if __name__ == '__main__':
            msgFive = 'DIAMOND UNBREAKABLE SWORD \nSHING'
            messageFive(msgFive)
answer = input()
if answer == "c":
    print("Life Bar:3")
    print("DIAMOND UNBREAKABLE SWORD \nSHING.  Press enter twice for Level 2")
else:
    print("Life bar:", 1 - 1, "\nGAME OVER\nTo try again, restart the program\nRetry button will be added in future")
    print(" updates and a proper health bar.")

    def ending(sting):
        for ending in "Thanks for playing ":
            print(ending, end="")
    if __name__ == '__main__':
        end = "Thanks for playing"
        ending(end)
answer = input()
nextLevel = True
while nextLevel:
    answerTwo = input()
    input("Are u ready for level two, if yes type Ready, for exiting the game press Enter")
    if answerTwo != 'Ready':
        nextLevel = False
        print("Level Two: Lol, you though there was a level two.  End Game")
    else:
        print("End of game")