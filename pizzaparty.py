def solve(a,b):
    for i in range(b,a+1):
        if a%i==0:
            return sum(int(x) for x in str(i))
    return -1
a,b=list(map(int,input().split()))
print(solve(a,b))