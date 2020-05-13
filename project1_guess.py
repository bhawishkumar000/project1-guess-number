
# seed the pseudorandom number generator
from random import seed
from random import randint
guess=3

value = randint(0, 10)
print(value)
while guess >0 : 
	inp=input("Please enter the first guess : " )
	inpt=int(inp)
	guess=guess-1
	if value == inpt:
		print("your choice is right",value)
	else: 
		if value > inpt:
			print("enter a higher  number")
		else :
			print("enter a lower number ")	
		continue	
