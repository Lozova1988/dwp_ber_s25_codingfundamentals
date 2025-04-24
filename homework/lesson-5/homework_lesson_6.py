#Task  $1
import random
rand_numbers=[]
for x in range(10):
    number=random.randint(1,100)
    rand_numbers.append(number)
print("Random numers are: ", rand_numbers)

sum_numbers=0
for num in rand_numbers:
    sum_numbers+=num

average= sum_numbers/len(rand_numbers)
print("Result of average of the numbers is: ", average)

import statistics
average2=statistics.mean(rand_numbers)
print("Result of average statistics is", average2)

#Task §2

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Mistake: you cannot divide on null"
    else:
         return a/b
    
operation = input("Choose operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation=="+":
    result=add(num1,num2)
elif operation=="-":
    result=sub(num1,num2)
elif operation=="*":
    result=mult(num1,num2)
elif operation=="/":
    result=div(num1,num2)
else:
    result = "Mistake: unknown operation"

print("Result is: ", result)


#Task 3 This was completely done by the chat GPT, I don't have enough brains   :(

def generate_number():
    return random.randint(1,100)

def get_user_guess():
    guess = input("Guess a number from 1 to 100: ")
    return int(guess)

def check_guess(secret,guess):
    if guess<secret:
        print("Too little!")
        return False
    elif guess>secret:
        print("Too big!")
        return False
    else:
        print("You are win!")
        return True
    
def play_game():
    secret_number = generate_number()
    tries=0
    max_tries=5
    while tries<max_tries:
        guess=get_user_guess()
        tries+=1
        if check_guess(secret_number,guess):
            print("You are win")
            break
    else:
        print("Game over! The number was: ", secret_number)

play_game()



