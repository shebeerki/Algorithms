def heapSort(a):
     	def sift(start, count):
         	root = start
 
         	while root * 2 + 1 < count:
             		child = root * 2 + 1
             		if child < count - 1 and a[child] < a[child + 1]:
                 		child += 1
             		if a[root] < a[child]:
                 		a[root], a[child] = a[child], a[root]
                 		root = child
             		else:
                 		return
 
     	count = len(a)
     	start = count / 2 - 1
     	end = count - 1
 
     	while start >= 0:
         	sift(start, count)
         	start -= 1
 
     	while end > 0:
         	a[end], a[0] = a[0], a[end]
         	sift(0, end)
         	end -= 1
	return a

a = input("enter the list\n")
print "%r\n"%heapSort(a)
 

