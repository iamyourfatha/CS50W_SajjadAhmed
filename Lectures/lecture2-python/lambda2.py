people = [
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# a condensed method
people.sort(key=lambda person: person["name"])

print(people)