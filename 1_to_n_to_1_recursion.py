n=int(input("enetre a num:"))
def pnum(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    pnum(n,m+1)
    if m!=0:
        print(m,end=" ")
pnum(n)