def quicksort(a):
	if len(a) <= 1:
		return a
	length = len(a)
	pivot = a[length / 2] 
	less = []
	greater = []
	for i in range(length):
		if i == length / 2:
			continue
		if a[i] < pivot:
			less.append(a[i])
		else:
			greater.append(a[i])
	return quicksort(less) + [pivot] + quicksort(greater) 

lis = input("enter the list\n")
print "%r\n"%quicksort(lis)
