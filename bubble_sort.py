

#bubble sort
li=list(map(int,input().split()))
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)