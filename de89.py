"""a="hello ramana"
print(" ".join(a.split()[::-1]))
print([i for i in range(1,11) if i%2!=0])

n=int(input("enter a number to check prime"))
flag=0
for i in range(2,(n//2)+1):
    if n%i==0:
        print("not prime")
        flag=1
        break
if flag==0:
    print("prime")

"""
'''45

    
st="apple"
a={}
for i in st:
    if i not in a:
        a[i]=1
    else: a[i] +=1
print(a)

#print(sum(map(int, input())))
n=int(input("enter a number to sum of digits"))
rem=0

while n>0:
    rem+=n%10
    n=n//10
print(rem)
    
 
    
s=input("enter a stringtng to reverse vowels in that : ")
vow="aeiouAEIOU"
st=[i for i in s if i in vow]
print(st)
re=""
for i in s :
    if i in vow:
        re+=st.pop()
    else:
        re+=i
print("reverse vowels in string : ",re)

s=input("enter a stringtng to reverse vowels in that : ")
vow="aeiouAEIOU"
l=0
r=len(s)-1
li=list(s)
while l<r:
    if li[l] not in vow:
        l+=1
    elif li[r] not in vow:
        r-=1
    else:
        li[l],li[r]=li[r],li[l]
        l+=1
        r-=1
res="".join(li)
print("reverse vowels in string : ",res)
    
  
   
s="a@b#c$d"
li=list(s)
print(li)
l=0
r=len(li)-1
while l<r:
    if not li[l].isalpha():
        l+=1
    elif not li[r].isalpha():
        r-=1
    else:
        li[l],li[r]=li[r],li[l]
        l+=1
        r-=1
res="".join(li)
print("reverse vowels in string : ",res)

 '''
 
s=input("enter a string :")
res=[s[0]]
for i in range(1,len(s)):
    if s[i]!=res[-1]:
        res.append(s[i])
print('result = ',"".join(res))
 
 
s=input("enter a string :")
res=""+s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        res+=s[i]
print("result= ",res)
    
 
 
 
 
        