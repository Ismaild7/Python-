n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
 if i in d:
     d[i]+=1
 else:
     d[i]=1
print(d)         
lis=list(d.values())
print(lis)
mx=max(lis)
print(mx)
if lis.count(mx)>1:
    print(-1)
else:
    print(mx)   
       