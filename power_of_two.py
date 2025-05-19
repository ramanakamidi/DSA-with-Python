#power of two
n=int(input("enter a number to check power of two"))
if n<=0:
    print(False)
while n:
    if n==1:
        print(True)
        return
    if n%2!=0:
        print(False)
        return
    n=n//2
print(False)