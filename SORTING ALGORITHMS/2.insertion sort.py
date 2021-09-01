def insertionsort(l):
    for ele in range(len(l)):
        pos=ele
        while(pos>0 and (l[pos]<l[pos-1])):
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
    return l
#print(insertionsort([10,12,4,10,8,13]))
l=list(range(5000,0,-1))
print(insertionsort(l))


""" Here it gets the output a little bit quicker than before.
Since it checks every element before going into loop
But in the both cases Time complexity is  O(n^2) . It isn't feasible for n over 5000
Here comes the other one Merge Sort """
