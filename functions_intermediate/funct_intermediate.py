x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

u = [[2,5,6],[7,9,3,0],[7,7,7,7]]
def change_val(list):
    list[1][0] = 15
    return list

print(change_val(x))
print(change_val(u))

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_last_name(list):
    list[0]["last_name"] = "Bryant"
    return list

print(change_last_name(students))

# 3. In the sports_directory, change 'Messi' to 'Andres'
def sports_greats(dict):
    dict["soccer"][0] = "Andres"
    print(dict["soccer"])
    return dict

print(sports_greats(sports_directory))

# 4 .Change the value 20 in z to 30
def change_to_30(list):
    list[0]["y"] = 30
    return list

print(change_to_30(z))


# 2.

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
def iterate_Dictionary(list):
    for i in list:
        print(i)

print(iterate_Dictionary(students))  # also prints None
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# #3.
def iterate_dictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])


iterate_dictionary2("first_name", students)
iterate_dictionary2("last_name", students)
# 4.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dict):
    for i in some_dict:
        print(i, len(i), some_dict[i])


print_info(dojo)
def printInfo(some_dict):
    for item in some_dict:
        num_locations = len(some_dict[item])
        print(f"\nThere are {num_locations} {item}\n")
        for value in some_dict[item]:
            print(value)
        

printInfo(dojo)