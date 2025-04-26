for column in range(1, 4):
    print("| ", end="")
    for row in range(1, 4):
        print(row * column, end=" | ")
    print()
    print("-"*13)
print( )
for column in range(1, 6):
    print("| ", end="")
    for row in range(1, 6):
        print(row * column, end=" | ")
    print()
    print("-"*25)

print( )
x=int(input("Decide the size of the table: "))
for column in range(1,x+1):
    print("| ", end="")
    for row in range(1,x+1):
        print(row * column, end=" | ")
    print()
    print("-"*25)