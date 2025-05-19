li=[3,5,1,3,7,8,2,0,3,5]  
m1=0

for i in li:
    if li[i]>m1:
        m1=li[i]
m2=0
for i in li:
    if i>m2 and i!=m1:
        m2=i
print(m2)