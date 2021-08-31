def selectionsort(l):
    for start in range(len(l)):
        for i in range(start+1,len(l)):
            minpos=start
            if(l[i]<l[minpos]):
                (l[start],l[i])=(l[i],l[start])
    return l
""" l=[10,12,14,9,8,13]               
 """
l=list(range(5000,0,-1))
print(selectionsort(l))
