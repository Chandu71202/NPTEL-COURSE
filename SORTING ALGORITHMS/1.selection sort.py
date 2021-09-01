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

"""(This works well and good for values below 3000 when we give 5000 numbers in a list
it takes so a little time for running . if we consider in a real world scenario out of 1 lakh number such that
it takes so much time to execute . 

Here we go into another strategy known as insertion sort """
