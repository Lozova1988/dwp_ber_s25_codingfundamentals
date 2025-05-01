items_list = []
while True:
    item=input("Enter items for shopping list (Tipe `done` to finish): ").strip( )
    if item == "":
        continue
    if item.lower() =="done":
        break
    items_list.append(item)
items_list.sort()   
print(f"Your shopping list is: ", items_list)

counter = 1
for item in items_list:
    print(str(counter)+". "+ item)
    counter=counter+1

print("Total number of items: " + str(len(items_list))) 