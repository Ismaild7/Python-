n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m1,m2=arr[-1],arr[-2]
av=(m1+m2)/2
s=0
for i in range(n):
    if arr[i]>=av:
        s+=arr[i]
    else:
        a[i]=0    
print(s)
print(arr)        