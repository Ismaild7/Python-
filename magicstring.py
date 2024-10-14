def magic_string(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    max_freq=0
    for count in char_count.values():
        if count>max_freq:
            max_freq=count
    min_step=len(s)-max_freq
    return min_step                            
s='aaabbbccdddd'
print(magic_string(s))            