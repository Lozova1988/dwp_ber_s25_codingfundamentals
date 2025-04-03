scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print("The length of scores is:  ", len(scores))

count_three=scores.count(3)
print("Count of number 3 is: ", count_three)

print("Maximum in scores is:  ", max(scores))

list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
comm_elements=set(list_1)&set(list_2)
print("The common elements are:  ",comm_elements)

all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers=list()
for numer in all_numbers:
    if numer>0:
        positive_numbers.append(numer)
print("Positive numbers are: ", positive_numbers)


reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print("List in reverse: ", reverse_this_list)



new_scores=set(scores)
print("New set is:  ", new_scores)

tuple_country = [("Germany", "Berlin"),("Ukraine","Kyiw"), ("England", "London"),("France", "Paris"), ("Poland", "Warschaw" )]
print("Countries and capitals: ", tuple_country)