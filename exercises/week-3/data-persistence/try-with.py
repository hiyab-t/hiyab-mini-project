pets = ['rani', 'susu', 'ruba']

try:
    with open('saved_pets.txt', 'w') as file_handle:
        for pet in pets:
            file_handle.write(pet)
    print('File saved')
except Exception as whoops:
    print(f'problem saving file: {whoops}')
