my_first_dictionary = {
    "name":"Olena", 
    "age":37, 
    "occupation":"student"
}

my_first_dictionary["hobbies"] = ["swimming", "reading"]
#print("using get: ")
#print(my_first_dictionary.get("occupation"))
#print("without get: ")
#print(my_first_dictionary["occupation"])

#print(my_first_dictionary.get("nationality"))


if "nationality" in my_first_dictionary:
     print(my_first_dictionary["nationality"])
else:
     print("Unknown")

#print(my_first_dictionary.keys())

#print(my_first_dictionary.values())

my_first_dictionary["occupation"] = "intern"
#print(my_first_dictionary)

my_first_dictionary.pop("age")
#print(my_first_dictionary)

"Favorite Color" in my_first_dictionary

incomes = {
     "Mother": 3600.00, 
     "Father": 2500.00, 
     "Daughter": 500.00
}
accumulator = 0
for income in incomes.values():
     accumulator = accumulator + income

#print(accumulator)

my_dict = {
     "name": "Rapunzel",
     "age": 19,
     "hobbies": ["paiting", "singing", "reading"]
}
 
#for key in my_dict.keys():
#      print(key)
 
#for value in my_dict.values():
#      print(value)
 
#for k, v in my_dict.items():
#     print(k, "---->", v)

conv_list = []
for key, val in my_dict.items():
     conv_list.append((key, val))
print(conv_list)

my_personal_dict = {
     "name":"Olena",
     "hobbies":"reading",
     "age":20
}

my_friends_dict = {
     "name":"Lala",
     "hobbies":"swimminf",
     "age":30
}
my_friendschip_list = [my_personal_dict, my_friends_dict]
total_sum = 0
for dictionary in my_friendschip_list:
     total_sum += dictionary.get("age")
average = total_sum / len(my_friendschip_list)
print(average)