s = input("enter numbers:\n")
n = list(map(int, s.split()))
for i in range (0, len(n) - 1):
	minIndex = i
	for j in range (i+1, len(n)):
		if n[j] < n[minIndex]:
			minIndex = j
		if minIndex != i:
			n[i], n[minIndex] = n[minIndex], n[i]
			
print ("Sorted array:")
for i in range(len(n)):
    print ("%d" %n[i])