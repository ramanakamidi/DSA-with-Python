#sort even first and odd next

li=[3,5,1,3,7,8,2,0,3,5]
li.sort()
res=[]
for i in li:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)