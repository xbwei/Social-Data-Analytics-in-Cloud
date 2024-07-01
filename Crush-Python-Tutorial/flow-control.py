'''
flow control
'''

# whitescape 

print(1  
        + 22)  #whitespaces in parentheses and brackets are ignored 
        
my_demo = 2+\
        2       #use backslash to continue a new line  
print(my_demo)


# object id vs. value

list_a = [1,2,3] 
list_b = [1,2,3]

print(id(list_a)) #get the id of a list variable
print(id(list_b))

print(list_a is list_b) #compare the ids of two variables
print(list_a==list_b) #compare the values of two variables


# Boolean and None

print(False and True) #return False
print(False or True) # return True
print(not False) # return True

print(not []) #empty list is False, therefore not [] return True
print(not None) #None is False, therefore not None return True

# if-else statement

if 2>1:  # the condition is true
    print('2 is great then 1') #this code will be executed

else:
    print('2 is less than 1') #this line will be ignored

print('not in the flow control') #this line will always be printed as it is not inside an if-else statement


# for loop

for number in [1,2,3]:
    print(number)

# for loop and range function

for number in range(1,7,2): #it will start from 1, end at 6 (7-1) with an increment of 2 
    print(number)           #it will print 1, 3 (1+2), and 5 (1+2+2)


# while loop

number = 1  #define the initial value to be 1

while number <=5:  # condition is the number is less or equal to 5

    number = number + 1 # change the number value to avoid a dead loop
    
    print(number)
    

# while loop and break/continue/pass statement

number = 1  

while number <=5:  

    number = number + 1 
    
    if number ==3:
        continue    # try to use pass or break to see what will happen
    print(number)
    
    