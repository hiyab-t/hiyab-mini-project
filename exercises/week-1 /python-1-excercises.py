
#part 1

#1
first_name = "Hiyab"

print(first_name)

#2 and 3
last_name = "Tewelde"

print(f"Hi, my name is {first_name} {last_name}.")

#integers

#1 and 2
x = 3
y = 4

product = (x*y)

print(f"The product of {x} and {y} is {product}.")

#lists

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

third_person = people[2]

print (third_person)

fifth_person = people[-3]

print(fifth_person)

new_people_list = ["Mark", "Lisa" , "Joe", "Barry"]

print(people[6] == new_people_list[3])

#input

name = input("Input your name: ")

print (f"Your name has been saved as {name}.")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

product = num1 * num2 

print(f"The product is {product}.")

#part 2 

#input and numbers

#1 and 2
chosen_num = int(input("Input a number: "))

if chosen_num % 2 == 0 and chosen_num % 4 == 0 :
    print("This number is even and multiple of four.")
elif chosen_num % 2 == 0:
    print ("This number is even but not a multiple of 4.")
else:
    print ("This number is odd and not a multiple 4.")

#3
chosen_number= int(input("Input a number: "))

if chosen_number % 3 == 0:
    print("fizz")
elif chosen_number % 5 == 0:
    print("buzz")
else:
    print(" ")


#Temperature conversion

#1

temp =  [ "f", "c"]

chosen_temp = input(f"Choose a temprature unit from {temp} and input a correspording letter: ")

chosen_num = int(input("Input a number that you would like to convert: "))

if chosen_temp in temp[0]:
    print(((chosen_num * 1.8) + 32), chosen_temp)

elif chosen_temp in temp[1]:
    print(((chosen_num - 32)* (5/9)), chosen_temp)
else:
    print("Error encountered while computing. Please ensure you are follwing and instructions and entering the appropriate character.")

#part 3

#1
"""
and is an operator which is used when either side of conditions need to be met 
or elese it is false. Or operator is used when one of the either conditions need 
to be met. not is used as a negator of a condition.
"""

#2
"""
false
true
true
true
"""

#3
'''
false
false
false
true
'''
#4

#5

user_age = int(input("What is your age? "))
salary_amount= int(input("What is your annual salary? "))

if user_age > 21 and salary_amount >= 21000:
    print("You can loan up to £50,000.")
elif user_age > 30 and salary_amount >= 35000:
    print("You can loan up to £75,000.")
elif user_age > 30 and salary_amount >= 50000:
    print("YOu can loan up to £100,000.")
else:
    print("You do not meet the minimum requirements to be offered a loan.")



#tuna

foods = ["tuna", "salmon", "mackerel", "trout"]
side_dish = ["chips", "chocolate", "broccoli"]

chosen_food = input(f"Choose from {foods}")

if chosen_food.lower() in foods[1:] :
    print(f"Okay, {chosen_food} is noted.")
else:
    print(f"Aw, we are out of tuna! Maybe tommorow. But you can choose from {foods[1:]} with some side dishes.")

chosen_side_dish = input(f'What would you like on the side? There is {side_dish}')

if chosen_side_dish.lower() in foods[1:]:
    print(f"{chosen_food} with {chosen_side_dish} coming right up!" )





