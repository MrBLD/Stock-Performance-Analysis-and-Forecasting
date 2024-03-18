# create all data types(name(capitalize), phone number(add +91), email(only accept of given format else give error), and all similar) and merge it in all form of datasets(sets, lists, tuples, dictionary, and all similar), make username from email, num1, num2, num3 with and without typecasting

#     take the input on one number list in the form a: 1,b: 2 and assign accodingly
#     divide all numeric dataset by 10(taken as input) and store remainder at their places
#     make one dataset with index as dataset name its index in that data set along with value
#         make a copied dataset of all multiple of 10 from all datasets
#             using all
#             using previously stored indices
#     find which numeric dataset has highest mean square value
# export all the datasets to files: txt, csv, excel

import re
# import pandas as pd

# Define the data types
name = "john doe"
phone_number = "1234567890"
email = "johndoe@example.com"
num1 = 42
num2 = 3.14
num3 = complex(1, 2)

# Perform data type conversions if needed
num1_str = str(num1)
num2_int = int(num2)
num3_str = str(num3)

# Manipulate the data to fit the desired format
name = name.title()  # capitalize the name
phone_number = "+91" + phone_number  # add +91 prefix to phone number
username = email.split("@")[0]  # extract username from email

# Validate the email address format
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Error: Invalid email address")

# Combine the data into different data structures
list_data = [name, phone_number, email, username, num1, num2_int, num3]
tuple_data = (name, phone_number, email, username, num1_str, num2_int, num3_str)
set_data = {name, phone_number, email, username, num1, num2_int, num3}
dict_data = {
    "name": name,
    "phone_number": phone_number,
    "email": email,
    "username": username,
    "num1": num1,
    "num2": num2_int,
    "num3": num3_str
}

var_dict = {}

for var_name in dir():
    var_list = eval(var_name)
print(var_list)

for var_name in dir():
    if not var_name.startswith("_"):
        var_dict[var_name] = eval(var_name)
print(var_dict)


# Take input of a number and divide all numeric data sets by it
divisor = int(input("Enter a divisor: "))
num1_rem = num1 % divisor
num2_rem = num2_int % divisor
num3_rem = num3.real % divisor

# Create a new data set with index as the name of the original data set,
# and the value as the original index and the remainder after division
merged_data = {}
merged_data["list_data"] = [(i, x % divisor) for i, x in enumerate(
    list_data) if type(x) in [int, float, complex]]
merged_data["tuple_data"] = [(i, float(x) % divisor) for i, x in enumerate(
    tuple_data) if type(x) == str and x.isdigit()]
merged_data["dict_data"] = [
    (i, x % divisor) for i, x in dict_data.items() if type(x) in [int, float, complex]]

# Create a copy of all multiples of 10 from the original data sets
multiples_of_10 = []
for data in [list_data, tuple_data, set_data, dict_data]:
    multiples_of_10.extend([x for x in data if type(
        x) in [int, float, complex] and x % 10 == 0])

# Alternatively, create a copy of all multiples of 10 from the merged data set
multiples_of_10_merged = [x for _, x in merged_data.values() if x % 10 == 0]

# Find which numeric data set has the highest mean square value
mean_square = {}
mean_square["num1"] = num1 ** 2
mean_square["num2"] = num2 ** 2
mean_square["num3"] = num3.real ** 2
mean_square["num1_rem"] = num1_rem ** 2
mean_square["num2_rem"] = num2_rem ** 2
mean_square["num3_rem"] = num
