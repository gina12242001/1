"Gina"
# for i in range(1,30):
# 	print i


def function(x):
	answer = 0
	for i in range(0, len(str(x))):
		answer = (x % 10) + answer   
		x = x / 10 
		print answer 

	return answer
	
print function(1234)













def multiply(x):
	finalanswer = 1
	for i in range(0,len(str(x))):
		finalanswer = x % 10 * finalanswer
		print finalanswer
		x = x / 10 
		print finalanswer
	return finalanswer

print multiply(1234)

