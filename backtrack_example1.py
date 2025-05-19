#path backtracking
def path(m,i,j,p,n):
    if i==n-1 and j==n-1:
        print(p)
        return
    if i+1<n and m[i+1][j]==1:
        path(m,i+1,j,p+"d",n)
    if j+1<n and m[i][j+1]==1:
        path(m,i,j+1,p+"r",n)


m=[[1,1,1,0],
   [0,1,1,0],
   [0,1,1,1],
   [0,0,0,1]]
path(m,0,0,"",len(m)) 