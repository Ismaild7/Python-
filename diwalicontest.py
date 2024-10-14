#ip an integer n,represents total no. of problems
#p time to travel
n=int(input())
p=int(input())
t=240-p
c=0
for i in range(1,n+1):
    if t>0 and t>i*5:
        t=t-(i*5)
        c+=1
    else:
        break
print(c)        
        
        