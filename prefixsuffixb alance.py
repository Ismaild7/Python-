def find_absolute_diff(N,A):
    result=[]
    total_sum=sum(A)
    first_part_sum=0
    for i in range(N):
        first_part_sum+=A[i]
        second_part_sum=total_sum-first_part_sum
        difference=abs(first_part_sum-second_part_sum)
        result.append(difference) 
    return result
N=5
A=[1,2,3,4,5]
print(find_absolute_diff(N,A))     