arr=list(map(int,input().split()))
c=0
total=0
for move in arr:
    if move==1 or move==-1:
        total+=move
        if total==0:
         c+=1
print(c) 
     
     
     
# arr=list(map(int,input().split()))
# c=0
# total=0
# for move in arr:
#     if sum(arr[:move+1])==0:
#        c+=1    
# print(c) 
     