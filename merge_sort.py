
#merge sort
def div(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=div(arr[:mid])
    right=div(arr[mid:])
    return merge(left,right)
def merge(left,right):
    i=0
    j=0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    print(res)
    return res
arr=[2,0,9,8,3,4,8,5]
print(div(arr))