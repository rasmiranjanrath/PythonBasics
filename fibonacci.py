#fibonasi series
first_number=0
second_number=1
sum=0
for i in range(5):
	sum=first_number+second_number
	print(sum)
	first_number=second_number
	second_number=sum
