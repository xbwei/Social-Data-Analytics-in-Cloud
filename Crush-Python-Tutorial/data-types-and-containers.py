"""
data types and containers
"""

#Introduce the basic data types and containers in Python

# basic data types 

print(type("123"))
print(type(123))
print(type(123.))

# common string methods

print("Hello, World".upper()) #change to upper cases
print("Hello, World".lower()) #change to lower cases

print("  Hello, World  ") #a string with spaces on both side
print("  Hello, World  ".strip()) #strip spaces on both sides 

print("Hello, World".split()) #split the string by space
print("Hello, World".split(',')) #split the string based on ,

print("Hello, " + "World") #concatenate two strings

print(len("Hellow, World")) #count the number of characters
print("Hellow, World"[0]) #print the first character

# number calculation 

print(2+3) #sum
print(2-3) #difference
print(2*3) #product 
print(2**3) #power
print(2/3) #division

# define variables

my_name = "Andrew"
print(my_name)

my_name = "Andy"
print(my_name)

# define a list

my_list =[1,1,3,4] #define a list
print(my_list)

my_nested_list = [1,1,3,4,[1,2]] #define a nested list
print(my_nested_list)

print(my_list[1:3]) #print the 2nd and 3rd item

my_list[0]=0 #change the value of the first item
print(my_list)

#list methods

my_list.append(7) #add an item to a list
print(my_list)

my_list.remove(3) #remove an item from a list
print(my_list)

my_list.sort() #sort the items in a list
print(my_list)

my_list.reverse() #reverse the list order
print(my_list)

print(my_list+my_nested_list) #combine two lists
print(len(my_list)) #count the number of items in a list
print(7 in my_list) #check if an item in a list

# set and tuple

my_set = {1,1,3,4} #define a set
print(my_set) #duplicated items are removed

my_tuple = (1,) #define a tuple
print(type(my_tuple)) #this is a tuple

not_a_tuple = (1) #this is not a tuple
print(type(not_a_tuple)) 

# my_tuple[0] = 2 #this will create an error



# define a dictionary 
my_tweet = {
        "tweet_id":1138,
        "coordinates": (-75, 40),
        "visited_countries": ["GR", "CH", "MY"]
        }
        
 
 
print(my_tweet['visited_countries']) #this equals to the list of ["GR", "CH", "MY"]      

print(len(my_tweet['visited_countries'])) #use len() function to count the number in the list 

print("US" in (my_tweet['visited_countries'])) #use in operator to check whether 'US' in the list

# dictionary methods

print(my_tweet.keys()) #print all the keys in a dictionary
print(my_tweet.values()) #print all the values in a dictionary

my_tweet['text']='hello world' #add a new key-value pair
print(my_tweet) 
