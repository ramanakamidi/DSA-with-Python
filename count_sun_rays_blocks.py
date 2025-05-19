li=[2,3,4,3,2,3,5,4,2]
max=0
c=0
for i in range(len(li)):
    if li[i]>max:
        print(li[i])
        max=li[i]
        c+=1
print("count=",c)