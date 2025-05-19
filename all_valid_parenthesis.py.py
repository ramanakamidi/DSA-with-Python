 #binary of nums
def par(n,o=0,c=0,res=""):
    if 0==n or c==n:
        print(res)
        return
    if o<n:
        par(n,o+1,c,res+"(")
    if c<o:
        par(n,o,c+1,res+')')
n=3
par(n)