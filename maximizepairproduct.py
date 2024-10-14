n=int(input())
arr=list(map(int,input().split()))
d=[]
pro=0
k=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==18:
            if arr[i]>arr[j]:
                k=arr[i]*arr[j]
                if k>pro:
                    pro=k
                    d.append(arr[i])
                    d.append(arr[j])
print(d)                    