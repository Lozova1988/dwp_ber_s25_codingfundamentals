from datetime import datetime
current_time=datetime.now()
day=current_time.day
month=current_time.month
year=current_time.year
hour=current_time.hour
minute=current_time.minute
second=current_time.second
today_date=current_time.strftime("%d.%m.%y")
today_time=current_time.strftime("%H:%M:%S")
print("Current date is: ",today_date,"Current time is: ",today_time)




def count_letters(text):
    count=0
    for x in text:
        if x.isalpha():
            count+=1
    print("The number of letters: ",count)

def count_letters_return(text):
    count=0
    for x in text:
        if x.isalpha():
            count+=1
    return count

count_letters("ghfkjhhlukgff")
result_1=count_letters_return("dsjhfjdhfjdh")
print("Saved number of letters: ", result_1)
#user_input=input("Enter text: ")

#count_letters(user_input)

#result=count_letters_return(user_input)
#print("Saved number of letters: ",result)

def funktion_sum(a,b):
    return a+b
result=funktion_sum(7,5)
    
def funk_div(c):
    if c%3==0:
        print("Parameter can be divided by 3")
    else:
         print("Parameter cannot be divided by 3")

funk_div(result)

import random
def play_game():
    choices = ["Rock","Paper","Scissors"]
    print("Choose one: 0 for Rock, 1 for Paper, 2 for Scissors")
    user_imput=input("Your choise: ")
    if user_imput not in ["0","1","2"]:
        print("Invalid iput")
        return
    user_choice=int(user_imput)
    computer_choise=random.randint(0,2)
    if user_choice==computer_choise:
        print("It is a Tie")
    elif (user_choice==0 and computer_choise==2) or \
        (user_choice==1 and computer_choise==1) or \
        (user_choice==2 and computer_choise==1):
        print("You win")
    else:
        print("You lose")
play_game()
