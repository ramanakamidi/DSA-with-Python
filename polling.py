n=int(input("enter number of candidates to votes"))
candidates=list(map(int,input().split()))
voters=list(map(int,input().split()))
c=[0]*max(candidates)
for i in range(n):
    if voters[i]>=18:
        c[candidates[i]-1]+=1
print(c)
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    m=max(c)
    print(c.index(m)+1)