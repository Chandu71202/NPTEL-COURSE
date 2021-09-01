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


""" Here it gets the output a little bit quicker than before.
Since it checks every element before going into loop
But in the both cases Time complexity is  O(n^2) . It isn't feasible for n over 5000
Here comes the other one Merge Sort """
