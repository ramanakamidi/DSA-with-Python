#recursion 1,2,3,4,5
n=int(input("enetre a num:"))
def pnum(n):
    if n==0:
        return
    pnum(n-1)
    print(n,end=" ")  
pnum(n)