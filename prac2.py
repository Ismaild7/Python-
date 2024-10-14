def count_freq(array):
    frequency={}
    for item in array:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency
array=list(map(int,input().split()))
frequency =count_freq(array)
print(frequency)            