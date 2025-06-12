
def firstMissingPositive(nums):
    sort=sorted(nums)
    l=len(sort)

    
    #Dealing with the negatives and zero

    if sort[l-1]<0:
        return 1

    i=0
    while sort:
        if sort[i]<=0:
            sort.pop(i)
            
        else:
            break
    
    #Side Case -1
    if sort==[]:
        return 1

    #Dealing With repeated numbers
    l=len(sort)

    i=0
    j=1

    while sort:
        if l==1:
            break
        if sort[i]==sort[j]:
            sort.pop(j)
            
        elif sort[i]!=sort[j]:
            i+=1
            j+=1
        if j>(len(sort)-1):
            break





    ####
    
    


    # Main Function
    l=len(sort)#new len

    for i in range(1,l+1):
        if i == sort[i-1]:
            pass
        else:
            return i

    return (sort[-1]+1)








print(firstMissingPositive([1]))