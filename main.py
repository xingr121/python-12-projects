import random

def guess(x):
    random_num= random.randint(1,x)
    guess=0
    while guess !=random_num:
        guess=int(input(f"guess a number between 1 and {x}"))
        if guess < random_num:
            print("sorry guess again, too low")
        elif guess > random_num:
            print("sorry, guess again, too high")
    print(f"congrats, you have guess the number {random_num} correctly")        
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low !=high:
           guess=random.randint(low,high)   
        else:
            guess=low
        feedback=input(f"is {guess} too high(h),too low(l),or correct(c)").lower()
        if feedback=='h':
            high=guess-1
        elif feedback== 'l':
            low=guess+1   
    print(f"the computer guessed your number {guess}")
computer_guess(10)        