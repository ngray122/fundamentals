# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Nicole"
print("Hello", name,"!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 35
print("Hello", 42,"!")	# with a comma
print("Hello " + str(42) + "!")	# with a +	-- this one should give us an error! /////TypeError
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "ice cream"
fave_food2 = "chicken wings"
my_fav_food = "I love to eat food."
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
print(my_fav_food.upper())
print(my_fav_food.title())
print(my_fav_food.endswith('.'))
print(my_fav_food.endswith('R'))
