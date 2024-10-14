#ip:-distance and position
#score=distance X position
#1.a subarray is acontiguous part of arry,2.assume 1 based indexing,3.the array conatains both psitive and 
#-ve value,
n=int(input())
p=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-1):
    temp=arr[i:p+i]
    k,s=1,0
    for j in temp:
        s=s+(k*j)
        k=k+1
    if s>mx:
        mx=s
print(mx)               
    
    