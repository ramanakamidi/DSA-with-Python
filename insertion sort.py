#insertion sort
li=list(map(int,input().split()))
for i in range(1,len(li)):
    k=li[i]
    j=i-1
    while j>=0 and li[j]>k:
        li[j+1]=li[j]
        j-=1
    li[j+1]=k
print(li)