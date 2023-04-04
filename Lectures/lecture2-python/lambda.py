people = [
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#if sorting by name
def f(person):
    return person["name"]
def h(person):
    return person["house"]


people.sort(key=f)
print(people)

people.sort(key=h)
print(people)