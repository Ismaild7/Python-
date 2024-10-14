s=input()
score=0
for i in s:
    if i=='H' or i=='h':
        score+=2
        if score==6:
            break
    if i=='T' or i=='t':
        score-=1
print(score)            