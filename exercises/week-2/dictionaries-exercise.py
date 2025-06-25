#1

friend = {
    'first_name': 'Meti',
    'last_name': 'Teshome',
    'age' : 22,
    'city': 'Addis Ababa'
}

print(friend)

#2

fav_nums = {
    'Maxi': 7,
    'Hiyab': 12,
    'Ebrar': 6,
    'Meti': 3,
    'Melat': 6
}

print(fav_nums)

#3

rivers = {
    'blue_nile':'Ethiopia',
    'amazon': 'Brazil',
    'yangtze': 'China'

}

for i in rivers:
    print()

#4

pets = {
    'rani' : {
    'owner' : 'hiyab',
    'kind_of_animal':'dog'
},

'ruba' : {
    'owner' : 'hiyab',
    'kind_of_animal': 'cat'
},

'susu' : {
    'owner' : 'hiyab',
    'kind_of_animal': 'cat'
},

'bobi' : {
    'owner' : 'hiyab',
    'kind_of_animal':'dog'
}
}

print('Known facts about the following pets.\n')
for x, obj in pets.items():
    print(f'{x}\n')

    for y in obj:
        print(f'{y}: {obj[y]}\n')

