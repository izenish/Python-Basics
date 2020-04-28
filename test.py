import os
clear=lambda:os.system('cls') #This is a comment 
print('helo')
clear
'''Multilined


Comment'''
print(256|255)
# | is OR and & is AND
# XOR = ^
print(222^255)
print("--------------Next Course--------------------------")
#If statements
str='namaste'
if str=="hello" or str=='namaste' :
	print('Helo how are you?')
	print('not indent')



print("--------------Next Course--------------------------")

#While, break and continue
while True:
	print('Infinite')
	break





print("--------------Next Course--------------------------")
#Functions
def dualcall():
	return("Return A",2)

ret=dualcall()
print(ret)

print("--------------Next Course--------------------------")
#error handling
#print(5/0) will show ZeroDivisionError


print("--------------Next Course--------------------------")
#Data input
''' Dont build if you want to enter, go to subllimerepl and python run command'''
'''age=input("how old are u:")
print("your age is:",age)'''

print("--------------Next Course--------------------------")
str="Hello"
str2= " world"
str3=" This is the third combination"
print(str+str2+str3)

#boolean true and false
a=False
b= True
print(a)
print(b)
#Boolean Inverse

x= not True
y= not False
print(x)
print(y)


print("--------------Next Course--------------------------")
# IN OPERATOR
animal="dog"
if animal in["lion",'dog','cat']:
	print("Your animal is in this array")