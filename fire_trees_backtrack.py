def fire(m,i,j):
    if not m:
        return
    if i<0 or j<0 or i>=len(m) or j>=len(m) or m[i][j]!=1:
        return
    m[i][j]=2
    fire(m,i+1,j)
    fire(m,i,j+1)
    fire(m,i,j-1)
    fire(m,i-1,j)

c=0
m=[[1,1,1,0],
   [0,1,1,0],
   [0,0,1,1],
   [1,0,0,1]]
fire(m,0,0)


for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]==1:
            c+=1
print(c)