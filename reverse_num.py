
#revere a number
n=int(input("enter a num to reverse"))
s=0
while n:
    r=n%10
    s=s*10+r
    n=n//10
print(s)
n=int(input("enter a num to reverse"))
def revNum(n,r=0):
    if n==0:
        return r
    r=r*10+(n%10)
    n=n//10
    return revNum(n,r)
print(revNum(n))