"""
data types and containers
"""

# basic data types 

print(type("123"))
print(type(123))
print(type(123.))

# common string methods

print("Hello World".upper()) #change to upper cases
print("Hello World".lower()) #change to lower cases
print("Hello World".split('W')) #split the string by 'W'

# variable

my_name = "Andrew"
print(my_name)

my_name = "Andy"
print(my_name)

# data containers

my_list =[1,1,3,4]
my_tuple = (1,1,3,4)
my_set = {1,1,3,4}
my_dic={
        "name": "Andy",
        "id":123}
        
# data container methods example

print(my_set) #only unique values are stored

print(my_tuple[0]) #print the first item in a tuple

my_list.reverse() #reverse the order of the list
print(my_list)

print(my_dic['name']) #print the value of the 'name' key