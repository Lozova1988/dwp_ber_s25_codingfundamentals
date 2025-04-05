def say_hallo(first_name, second_name):
    print("Hello "+ first_name +" "+ second_name+" are you ready for some fun coding today?")

say_hallo("Olena", "Lozova")

def repeat_charakter(charakter,number):
    counter=0
    result=""
    while counter<number:
        result+=charakter
        counter=counter+1
    print(result)
repeat_charakter("*",10)

