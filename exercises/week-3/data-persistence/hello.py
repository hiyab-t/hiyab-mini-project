try:
    file_handle = open('hello.txt', 'r')
    
    #text_content = file_handle.read()
    text_lines = file_handle.readlines()
    
    for line in text_lines:
        trimmed_line = line.strip()
        print(f'message from my dog is "{trimmed_line}"')
except FileNotFoundError as whoops:
    print(f'Could not find the file: {whoops}')

except Exception as whoops:
    print(f'Unexpected error: {whoops}')