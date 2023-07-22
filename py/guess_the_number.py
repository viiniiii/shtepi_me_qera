import random
def decrease_lives(lives):
    return lives - 1
difficulty = input("Zgjidhni nivelin e veshtirësisë: easy ose hard ")
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Zgjidh nje nga opsionet")
numri = random.randint(1,100)
global pick
pick = int(input("Zgjidhni nje numer: "))
while lives > 0 and pick != numri:
    if(pick > numri):
        print("Too high! Pick another number!")
        lives = decrease_lives(lives)
        print(f"You have {lives} lives left ")
        if lives > 0:
            pick = int(input())
    if(pick < numri):
        print("Too low! Pick another number!")
        lives = decrease_lives(lives)
        print(f"You have {lives} lives left ")
        if lives > 0:
            pick = int(input())
    if(pick == numri):
        print(f"The number was {numri}")
        print("You found it! Great job!")
        
if lives == 0:
    print("You lost!")
    print(f"The number was {numri}")  



