n=int(input())
if n%2!=0 or n==2:
    print(False)
else:
    n=n//2
    if n%2==0:
        print(n,n)
    else:
        print(n-1,n+1)