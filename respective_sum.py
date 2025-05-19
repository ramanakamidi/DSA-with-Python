li=[4,3,2,6]
ch=[[1,0,0,1],[1,0,0,0],[0,0,1,0],[0,1,1,0]]
for i in range(len(li)):
    s=0
    for j in range(len(ch[0])):
        if ch[i][j]==1:
            s+=li[j]
    print(s)