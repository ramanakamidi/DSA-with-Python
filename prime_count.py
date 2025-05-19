n=int(input("enterv a number"))
def checkPrime(val):
    for i in range(2,int(val**1/2)+1):
        if val %i ==0:
            return 0
    return 1
count=0
for i in range(2,n+1):
    count+=checkPrime(i)
print("count=",count)