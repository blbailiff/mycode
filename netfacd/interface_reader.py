#!/usr/bin/env python3


#This will import our new code
import netifaces
print(netifaces.interfaces())


#This will create a for loop, and iterate over netifaces.interfaces()
for i in netifaces.interfaces():
    #This will print a line the presents our interface
        print('\n**************Details of Interface - ' + i + ' *********************')
    #This will try printing the details of the interface we're checking out
try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
except:          # This is a new line
        print('Could not collect adapter information') # Print an error message



