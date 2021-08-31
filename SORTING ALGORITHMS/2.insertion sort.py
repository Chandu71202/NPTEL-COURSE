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