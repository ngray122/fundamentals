# Basic - Print all integers from 0 to 150.
def print1_to_150():
    for num in range(1, 151, 1):
        print(num)


print1_to_150()


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiple_of_5():
    for num in range(5, 1001, 5):
        print(num)


multiple_of_5()

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".


def print_dojo():
    for num in range(1, 101, 1):
        if num % 10 == 0:
            print("Coding Dojo")
        elif num % 5 == 0:
            print("Coding")
        else:
            print(num)


print_dojo()


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def add_odd():
    sum = 0
    for num in range(1, 500000, 1):
        if num % 2 == 1:
            sum += num
    print(sum)


add_odd()  # logs 62500000000


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countdown_by_4():
    for num in range(2018, 0, -4):
        print(num)


countdown_by_4()


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(lowNum, highNum, mult):
    for num in range(lowNum, highNum + 1):
        if num % mult == 0:
            print(num)


flexible_counter(2, 9, 3)