#file = open('people.txt', 'w')
#file.write('susan')
#file.close()

with open('pets.txt', 'r') as file_handle:
    text_content = file_handle.read()
    print(f'text = {text_content}')

print('all done')
