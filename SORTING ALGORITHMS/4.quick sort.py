import sys
sys.setrecursionlimit(10000)
def quicksort(l,left,right):
    if right-left <=1 :
        return l
    
    yellow=left+1
    for green in range(left+1,len(l)):
        if(l[green]<=l[left]):
            l[yellow],l[green]=l[green],l[yellow]
            yellow=yellow+1
    (l[left],l[yellow-1])=(l[yellow-1],l[left])
    quicksort(l,left,yellow-1)
    quicksort(l,yellow,right)
    return l
""" l=[1,5,3,6,4,2,7]
print(quicksort(l,0,len(l))) """

l=list(range(10000,0,-1))
print(quicksort(l,0,len(l)))