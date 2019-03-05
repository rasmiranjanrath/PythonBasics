listofbanana=['banana1','121','@#$%']
print(listofbanana)#printing whole list
print(listofbanana[0]) #printing specific  element at nth position
listofbanana[1]='banana2'#changing value at nth position
print(listofbanana[1])

listOfList=[[00,01,02],
			[00,77,99],
			[66,99,44]]; #list of lists
print(listOfList)

print(listOfList[1][0]) #printing values from a specific position


for x in listofbanana:
	print(x)           #print list using for loop

for y in listOfList:
	for z in y:         #print multi dimentional list
		print(z)


if 'banana2' in listofbanana:
	print('banana2 exists')    # check if perticular item exists

def findListLength(list):
	return len(list)
listofbanana.append('notabanana') #add an element
print(findListLength(listofbanana)) #check list length
listofbanana.remove('notabanana') # remove an element
print(findListLength(listofbanana))
print(findListLength(listOfList))

listofbanana.insert(1,'insertedbanana') # insert an element at nth postion
print(listofbanana)
del listofbanana[1] # delete an element from nth position
print(listofbanana)
listofbanana.pop() #removes last element if index not specifed
print(listofbanana)
del listofbanana  # delete  complete list