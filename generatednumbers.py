n,a,b=int(input()),int(input()),int(input())
unique_values=set()
for i in range(n):
    for j in range(n):
        reamining_value=n-i*a-j*b
        if reamining_value>0:
            unique_values.add(reamining_value)
print(len(unique_values))            
