#542 4 6 8 10
n=int(input("enetre a num:"))
def pnum(n):
    if n==0:
        return
    pnum(n-1)
    if n%2==0:
        print(n,end=" ")
pnum(n)