##from datetime import datetime
#current_time=datetime.now()
#day=current_time.day
#month=current_time.month
#year=current_time.year
#hour=current_time.hour
#minute=current_time.minute
#second=current_time.second
#today_date=current_time.strftime("%d.%m.%y")
#today_time=current_time.strftime("%H:%M:%S")
#print("Current date is: ",today_date,"Current time is: ",today_time)




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