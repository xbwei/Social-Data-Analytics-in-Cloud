"""
program design
"""

# try-except clause 

for number in range(5):
    try:
        print(1/(3-number))
    except:
        print('error')
        pass
    
# define a function

def calcuate_abs(input_value):
    if type(input_value) is str:
        return('wrong data type')
    elif input_value>=0:
        return(input_value)
    else:
        return(-input_value)
        
print(calcuate_abs("a"))
print(calcuate_abs(9))

# class and object

class car: # define a class
    maker = '' #define an attribute of the class
    
    def report_maker(self): #define a method, i.e., a function, of the class
        return(self.maker) #this method will return the maker attribute
        
my_car = car() #create an instance
my_car.maker = 'Tesla' #define the maker to be Tesla

print(my_car.report_maker()) #call the report_maker method

# import a library

import numpy

help(numpy)