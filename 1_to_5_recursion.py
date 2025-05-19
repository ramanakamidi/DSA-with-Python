#recursion 5,4,3,2,1
n=int(input("enetre a num:"))
def pnum(n):
    if n==0:
        return
    print(n,end=" ")
    pnum(n-1)
pnum(n)