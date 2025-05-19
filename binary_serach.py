#binary search
li=[1,3,5,6,7,8,9,34,67,87]
l=0
k=3
r=len(li)-1
m=(l+r)//2
while l<=r:
    m=(l+r)//2
    if li[m]==k:
        print(m,li[m])
        break
    elif k<li[m]:
        r=m-1
    else:
        l=m+1