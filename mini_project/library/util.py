def get_int_input(prompt_int, **kwargs):
    while True:
            try: 
                if int(input(prompt_int)) < 0:
                    raise ValueError('Negative numbers are not allowed')
            except ValueError as whoops:
                print(f'{whoops}. Please enter a valid number.')
            except IndexError as oops:
                print(f'{oops}. Please enter a valid number.')
            else:
                break 

def get_float_input(prompt_float, **kwargs):
    while True:
        if float(input(prompt_float)) < 0:
            print("No negative numbers. Please enter a valid number.")
        elif 'e' in float(input(prompt_float)):
            print("No scitentific notations please.") 