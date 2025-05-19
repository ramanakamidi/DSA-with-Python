#two pointer technique to merge
a=[3,5,6,8,9,10]
b=[2,4,7]
i,j=0,0
res=[]
while i<len(a) and j<len(b):
    if a[i]>b[j]:
        res.append(b[j])
        j+=1
    else:
        res.append(a[i])
        i+=1

if len(a)>len(b):
    res.extend(a[i:])
else:
    res.extend(b[j:])
print(res)