dictionary = { "vishali": "M.sc IT" }

for key,value in dictionary.items():
    print("%s --> %s" %(key,value))# dictionary[value]))
    
# some_key --> some_value



dictionary_tk = {
  "name": "vishali",
  "nickname": "vichu",
  "nationality": "india",
  "age": 23
}

for attribute, value in dictionary_tk.items():
    print("My %s is %s " %(attribute, value))
    
# attribute is a dictionary key prameter 


# dictionary = { "some_key": "some_value" }

# for key, value in dictionary.items():
#     print("%s --> %s" %(value, key))
# # C:\Users\visha\OneDrive\Desktop\sampleprogram.py


# Iterating over dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("% s % d" % (i, d[i]))
 
#  Using Zip() 
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
	print(fruit, "is", color)
 
