#bucket sort
a=[5,3,6,2,2,1,8,7,3,1,12]
k=4
res=[0]*(max(a)+1)
for i in a:
    res[i]=1
for i in range(len(res)-1,-1,-1):
    if res[1]==1:
        k-=1
    if k==0:
        print(i)
        break
print(res)