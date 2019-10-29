
the_array = [15, 22, 84, 14, 88, 23]
new_array = [] 
min_array = [] 


def maxy(aArray):
    i = 0
    for num in range(len(aArray)-1):
        if aArray[i] > aArray[i+1]: 
                new_array.append(aArray[i])
                i += 1
        else: 
            i += 1
    b = 0
    if new_array[b] > new_array[b+1]: 
        print(new_array[b])
    else: 
        print(new_array[b+1])

def miny(aArray):
    i = 0
    for num in range(len(aArray)-1):
        if aArray[i] < aArray[i+1]: 
                min_array.append(aArray[i])
                i += 1
        else: 
            i += 1
    b = 0
    if min_array[b] > min_array[b+1]: 
        print(min_array[b])
    else: 
        print(min_array[b+1])

maxy(the_array) 
miny(the_array)

print(maxy(the_array) -miny(the_array))

    
