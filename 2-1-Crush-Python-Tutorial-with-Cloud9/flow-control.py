'''
flow control
'''

# Boolean and None

print(False and True) #return False
print(False or True) # return True
print(not False) # return True

print(not []) #empty list is False, therefore not [] return True
print(not None) #None is False, therefore not None return True

# if-else statement

if 2>1:  # this is true
    print('2 is great then 1') #this code will be executed

else:
    print('2 is less than 1') #this line will be ignored

# for loop and range function

for number in range(1,5,2): #it will print 1 and 3 (1+2). 
    print(number)           #5 will not be printed as it is out of the range
    
# while loop and break/continue/pass statement

number = 1  #define the initial value to be 1

while number <=5:  

    number = number + 1 # try to comment this line and see what will happen
    
    if number ==3:
        continue    # try to replace pass or break to see what will happen
    
    print(number)
    
    