#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
fruits=('mango','orange','apple','banana')
print(fruits)
print(fruits[1])
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#loop through tuple
for f in fruits:
	print(f)

#check if an item is available or not

if 'mango' in fruits:
	print("present")

#find length
def find_tuple_length():
	return len(fruits)

print(find_tuple_length())

del fruits

fruits=tuple(('mango','banana','orange','apple'))
print(fruits)

print(find_tuple_length())