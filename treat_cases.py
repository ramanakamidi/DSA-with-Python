x=int(input())
a=list(map(int,input().split()))
police=0
untreated=0
for i in a:
    if i==-1:
        if police>0:
            police-=1
        else:
            untreated+=1
    else:
        police+=i
print(untreated)