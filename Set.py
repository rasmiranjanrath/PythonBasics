#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
set_of_link={'google.com','facebook.com','yahoo.com','jio.com'}

#loop through set
def loop_through_set():
	for links in set_of_link:
		print(links)

loop_through_set()
#check if item exists or not

if 'google.com' in set_of_link:
	print('yes')

#add an element to set
set_of_link.add('example.com')

loop_through_set()
#add multiple items to set

set_of_link.update(['random.com','gooje.com'])
loop_through_set()


