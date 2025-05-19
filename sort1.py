
li=[4,5,5,4,7,7,7,3,2,8,8,9,3,4,4]
dict={}
for i in li:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if dict[li[j]]>dict[li[j+1]]:
            li[j],li[j+1]=li[j+1],li[j]
        if dict[li[j]]==dict[li[j+1]] and li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)

