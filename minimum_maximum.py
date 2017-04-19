def find_max_min(a):
	min_max=[]
	minimum = a[0]
	maximum=a[0]
	for number in a:
		if minimum > number:
			minimum = number
			
		elif maximum<number:
			maximum=number
		# elif minimum==number and maximum==number:
		# 	b=(len(a))
	if minimum==maximum:
		min_max.append(len(a))
	else:
		min_max.append(minimum)
		min_max.append(maximum)
	return min_max
	
print (find_max_min([1, 2, 3, 4]))

