def answer(t, n):
    # no possible path to win
    if n-1>t:
        return 0
    # there is only one way to win. move right until end
    if n-1 == t:
        return 1
    # when n =2 or n==t there is t possible ways to win
    if n==2 or n==t:
        return t
    # when n is 3, there is a unique solution since you can only move left
    # on the middle path
    if n==3:
        return (2**(t-1)-1)%123454321
    # when n is 4, it is the sum of the pervious values 
    if n==4:
        return (2*(answer(t-1,n))+answer(t-2,n)+t-2)%123454321
    # all other cases are solved using trinomial expansion
    else:

        parentList = [1,1]
        childList = []
        total = 0
        for i in range(1,t-1):
            childList = []
            
            j=0 
            for j in range(0,n-1):   
                # first entry sum on the first and second of parent list  
                if j == 0:
                    childList.append(parentList[j] + parentList[j + 1])
                # all other entries, attempt to use trinomial expansion of parent list
                elif j<i+1:
                    # parent does not have a j+1 entry
                    if j+1>len(parentList)-1:
                        childList.append(parentList[j - 1] + parentList[j])
                    # trinomial expansion of the sums
                    else:                
                        childList.append(parentList[j - 1] + parentList[j] + parentList[j + 1])
                # set entry for the end of the expansion to 1 if current list size is 
                # between parentlist size and n-1
                elif j==i+1:
                    childList.append(1)
    
                # sum all entries in column
                if len(childList)==n-1:
                    total += childList[-1]
            
            parentList = childList
    
    return total % 123454321
