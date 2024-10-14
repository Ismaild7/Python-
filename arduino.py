a=list(map(int,input().split()))
n=len(a)
s=0
d=0
for i in range(n):
    s+=a[i]
    if abs(s)>d:
        d=abs(s)
print(d)    
    