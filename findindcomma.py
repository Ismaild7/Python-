n=int(input())
cur=1000
res=0
comma=1
while cur<=n:
    next=cur*1000
    numbers=min(n-cur+1,next-cur)
    res+=numbers*comma
    cur=next
    comma+=1
print(res)    