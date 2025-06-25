import random

#1

for numbers in range(0, 11):
    print(numbers)

#2

numbers = 0
while numbers <= 10:
    print(numbers)
    numbers += 1

#3

numbers_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]

for numbers in range(0, (len(numbers_list))):
    print(numbers_list[numbers])

#4

for num in range(11):
    if num < 11: 
        print(num)
else:
    print("done!")
    
#5

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for x in list1:
    for y in list2:
        if x==y:
            print(x)

#6

x = random.randint(1,100)

while 1==1:
    x += 1
    if x % 5 == 0:
        break
    elif x % 3 == 0:
        continue
    print(x)









