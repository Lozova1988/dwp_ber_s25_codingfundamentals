first_n=int(input("Enter first number"))
second_n=int(input("Enter second number"))
add=first_n+second_n
sub=first_n-second_n
mult=first_n*second_n
div=first_n/second_n
print("Sum of first and second numbers is ",add, ". Subtraktion of first and second numbers is  ",
      sub, ". Multiplikation of first and second numbers is  ",mult, ". Division of first and second numbers is  ", div )

numb=int(input("Enter number"))
div_by_3=numb%3
pow_of_2=numb**2
print("Remainder when divided by 3:   ", div_by_3,".  Number raised to the power of 2  ",pow_of_2 )


odd_or_even=int(input("Enter any number what you want "))
if odd_or_even%2==0:
    print("The number is even")
else:
    print("The number is odd")
    
first=int(input("Enter the first number   "))
second=int(input("Enter the second number   "))
if first>second:
    print("The first number is greater than the second")
elif first<second:
     print("The second number is greater than the first")
else:
    print("The two numbers are equal")



for counting_bis_10 in range(1,10):
    print(counting_bis_10)
    counting_bis_10=counting_bis_10+1


multipli=int(input("Enter the  number that you want multiply  "))
print("The number is  ", multipli)
for i in range(1,11):
    print(f"{multipli} x {i}=  ",multipli*i)

for buzz_fizz in range(1,21):
    if buzz_fizz%3==0 and buzz_fizz%5==0 :
        print("FizzBuzz")
    elif buzz_fizz%3==0:
        print("Fizz")
    elif buzz_fizz%5==0:
        print("Buzz")
    else:
        print(buzz_fizz)


leap_year=int(input("Enter a year:  "))
if leap_year%4==0 and leap_year%100!=0:
    print(leap_year," is a leap year")
elif leap_year%100==0 and leap_year%400==0:
    print(leap_year," is a leap year")
else:
     print(leap_year," is not a leap year")