# Python program to 
# demonstrate break statement 

# s = 'geeksforgeeks'
#  Using for loop 
# for letter in s: 

# 	print(letter) 
# 	# break the loop as soon it sees 'e' 
# 	# or 's' 
# 	if letter == 'e' or letter == 's': 
# 		break


# print("Out of for loop" ) 
# print() 
s = "vishali"
i = 0

# Using while loop 
while True: 
	print(s[i]) 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if s[i] == 'e' or s[i] == 's': 
		break
	i += 1

print("Out of while loop ") 

# Range method 

# Python Program to
# show range() basics

# printing a number
for i in range(10):
	print(i, end=" ")

# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
	sum = sum + i
print("\nSum of first 10 numbers :", sum)

# OutPut is : 45 the workflow is below
# Sum+ Range = total
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21
# 21 + 7 = 28
# 28 + 8 = 36
# 36 + 9 = 45










