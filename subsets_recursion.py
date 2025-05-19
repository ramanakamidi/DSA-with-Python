#subset

def subset(li,i,res=[]):
    if i==len(li):
        print(res)
        return
    subset(li,i+1,res+[li[i]])#take
    subset(li,i+1,res)#not take
       
    
li=list(map(int,input().split()))   
subset(li,i=0)   
