
#1 

def fun_1(num1, num2):
    return num1 + num2

print(fun_1(num1=345, num2=98))

#2

def fun_2(*nums):
    return nums[1] + nums[2]

print(fun_2(2, 3, 5, 6, 34, 4))

#3

def fun_3(**students):
    print(students)


fun_3(name1 = 'hiyab', student_id = 6396, is_married = False)

#bonus

#1, 2 and 3

def addition():
    return (f'Addition: {x + y}')

def subtraction():
    return (f'Subtraction: {x - y}')

def multiplication():
    return (f'Multiplication: {x * y}')

def division():
    return (f'Division: {x / y}')

def area_of_a_circle():
    return (f'Area of a circle: {2 * y * x}')

y = math.pi
# x = pow(2)

x = int(input("Inter the first number: "))
y = int(input ("Input the second number: "))

print(addition())
print(subtraction())
print(multiplication())
print(division())

#bonus fibonacci other ways


def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(7))

