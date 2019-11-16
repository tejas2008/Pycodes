s = input("enter numbers:\n")
n = list(map(int, s.split()))
for i in range(0,len(n)-1):
    for j in range(0,len(n)-1-i):
        if n[j] > n[j+1] :
            n[j],n[j+1] = n[j+1], n[j]
print ("Sorted array:")
for i in range(len(n)):
	print("%d" %n[i])
