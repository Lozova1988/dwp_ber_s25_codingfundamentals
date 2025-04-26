quota=1000
sum=int(input("Enter your quote"))
if sum>=quota:
    print("Done")
else:
    print("Not done")


quota=1000
sum=int(input("Enter your quote"))
if sum>=quota:
    print("0")
else:
    print(f"Quota is  {sum}")


def fruits_remaining(fruits_picked,fruits_quota):
    if fruits_picked>=fruits_quota:
        fruit_to_pick=0
    else:
        fruit_to_pick= fruits_quota-fruits_picked
        return fruit_to_pick

f=fruits_remaining(45,600)
print("You can pick else ", f)


