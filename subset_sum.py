def subset(li,k,i=0,res=[]):
    if i==len(li):
        if sum(res)==k:
            print(res)
        return
    subset(li,k,i+1,res+[li[i]]) #take
    subset(li,k,i+1,res) #not take
       
    
li=[1,2,3,4,5,8]
k=8
subset(li,k)