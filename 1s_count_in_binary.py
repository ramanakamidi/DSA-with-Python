
n=int(input("enter a num to check 1s in binary"))
c=0
while n:
    n=n & (n-1)
    c+=1
print(c)