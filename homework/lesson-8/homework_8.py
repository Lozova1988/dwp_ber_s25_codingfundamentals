european_cities = [
    ("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
    ("Moscow", [12678079, "Borscht", "Red Square"]),
    ("London", [8982000, "Fish and Chips", "Big Ben"]),
    ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
    ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
    ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
    ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
    ("Paris", [2140526, "Croissant", "Eiffel Tower"])
]

european_cities_info = {}

for city, info in european_cities:
    european_cities_info[city] = info

print("Dictionary of Cities:")
for city, info in european_cities_info.items():
    print(f"{city} --> {info}")

print("Sorted list of Cities:")
for city, info in sorted(european_cities_info.items()):
    print(f"{city} --> {info}")

berlin_info = european_cities_info.get("Berlin")
print("Info of Berlin:", berlin_info)

london_info = european_cities_info.get("London")
print("Type info of London:", type(london_info))


if "Barcelona" in european_cities_info:
    print("Info of Barselona:", european_cities_info["Barcelona"])
else:
    print("Barcelona: Not Found")

european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]
print("Add Rome: ")
for city, info in european_cities_info.items():
    print(f"{city} --> {info}")

removed_city = european_cities_info.pop("Madrid", None)
print("Delate Madrid:", removed_city)

if "Amsterdam" in european_cities_info:
    print("Amsterdam is in Dictionary.")
else:
    print("Amsterdam is not in Dictionary.")