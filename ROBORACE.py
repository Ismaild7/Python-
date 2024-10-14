import math
def find_meeting_time(x,n,y,m):
    lcm=(n*m)//math.gcd(n,m)
    for k in range(0,lcm*max(n,m)):
        t=x+k*n
        if(t-y)%m==0:
          return t
x=2
n=3
y=1
m=4
print(find_meeting_time(x,n,y,m))