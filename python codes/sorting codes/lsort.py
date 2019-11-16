s = input("enter numbers:\n")
n = list(map(int, s.split()))
for i in range(1, len(n)): 
     for j in range(i-1,-1,-1):
        if n[j] > n[j+1] :
            n[j],n[j+1] = n[j+1], n[j]
        else:
            break 

print ("Sorted array:")
for i in range(len(n)):
    print ("%d" %n[i]) 