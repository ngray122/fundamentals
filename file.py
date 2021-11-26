num1 = 42  # variable declaration, primitive data type-number
num2 = 2.3  # variable declaration, primitive data type-number
boolean = True  # variable declaration, primitive data type-Boolean
string = 'Hello World'  # variable declaration, primitive data type-string
# variable declaration, composite data type - list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, composite data type-dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable declaration, composite data type-tuples
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # type check, log statement
# access first index of pizza_toppings list, log statement
print(pizza_toppings[1])
# add value 'Mushroom' to pizza toppings list
pizza_toppings.append('Mushrooms')
# access name key and print value in person dictionary and log statement
print(person['name'])
# access name key in person dictionary and change the value to "George"
person['name'] = 'George'
# access the eye_color key in person dictionary change to "blue"
person['eye_color'] = 'blue'
print(fruit[2])  # access 2nd index in fruit tuple and log statement

if num1 > 45:  # conditional if statement. If num1 variable is greater than 45 (number)
    print("It's greater")  # log statement, string
else:  # conditional else statement
    print("It's lower")  # log statement, string

if len(string) < 5:  # conditional if statement, checks if length of string is less than (number) 5
    print("It's a short word!")  # log statement, string, if true
elif len(string) > 15:  # conditional else if, checks if length of string is greater than (number) 15
    print("It's a long word!")  # log statement, string, if true
else:  # conditional else
    print("Just right!")  # log statement, string

for x in range(5):  # for loop in range from 0-5 (numbers) not including 5, incrementing by 1
    print(x)  # log statement, print 0 1 2 3 4 
for x in range(2, 5): #for loop in range from 2-5 (numbers) not including 5, incrementing by 1
    print(x)  # log statement, print 2 3 4
for x in range(2, 10, 3):# for loop in range from 2-10 (numbers) not including 10, incrementing by 3
    print(x)  # log statement, print 2 5 8
x = 0 #variable declaration, primitive data type number
while(x < 5): #while loop, conditional statement. Stop when x is not less than 5
    print(x)  # log statement,
    x += 1 #increment 

pizza_toppings.pop() #delete last index of pizza_toppings
pizza_toppings.pop(1) #delete index one of pizza_toppings

print(person)  # log statement, person dictionary
person.pop('eye_color') # delete 'eye_color' key from person dictionary
print(person)  # log statement, person dictionary 

for topping in pizza_toppings: #for loop. Iterate through index in list
    if topping == 'Pepperoni': #conditional if statement 
        continue #continue if condition is met 
    print('After 1st if statement') # log statement,
    if topping == 'Olives': #if statement 
        break #if condition is true, break


def print_hello_ten_times(): #define function
    for num in range(10): #for loop, from numbers 0-9
        print('Hello')  # log statement, 10 times


print_hello_ten_times()#call function


def print_hello_x_times(x): #define function with 1 parameter
    for num in range(x): #for loop in range of x
        print('Hello')  # log statement


print_hello_x_times(4)#call function with 1 argument


def print_hello_x_or_ten_times(x=10): #define function, one parameter
    for num in range(x):# for loop in range of x
        print('Hello')  # log statement,


print_hello_x_or_ten_times()#call function - prints 10 times 
print_hello_x_or_ten_times(4)#call function with argument - prints 4 times


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined

# num3 = 72

# fruit[0] = 'cranberry'  - TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team']) -   KeyError: 'favorite_team'

# print(pizza_toppings[7]) - IndexError: list index out of range

#   print(boolean) - IndentationError: unexpected indent

# fruit.append('raspberry')  - AttributeError: 'tuple' object has no attribute 'append'

# fruit.pop(1)  - AttributeError: 'tuple' object has no attribute 'pop'


