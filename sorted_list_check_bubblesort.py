#bubble sort for sorted list checking
flag=False
li=[1,2,3,4,5]
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            falg=True
    if not flag:
        break
print(li)