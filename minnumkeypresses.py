#keyboard
s=input()
i=0
res=0
while i<len(s):
    if i<len(s)-1 and s[i]=='0'and s[i+1]=='0':
        i+=2
    else:
        i+=1
    res+=1
print(res)            
