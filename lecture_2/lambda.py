people = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {"name": "Cho", "house": "Ranenclaw"},
    {'name': 'Draco', "house": 'Slytherin'}
]


people.sort(key=lambda person: person['name'])

print(people)