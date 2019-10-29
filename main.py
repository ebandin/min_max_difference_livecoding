
the_array = [15, 22, 84, 14, 88, 23]


i = 0
for num in range(7): 
    if num[i] > num[i+1]: 
        num[i+1].pop() 
    i +=1 
    return num[i]

    
