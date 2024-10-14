n=int(input())
cnt=0
for a in range(0,int(n**0.5)+1):
    for b in range(0,int(n**0.5)+1):
        for c in range(0,int(n**0.5)+1):
            if(a**2+b**2+c**2+a*b+b*c+c*a==n):
                cnt+=1
                print(a,b,c)
print(cnt)                
        