l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i,len(l)):
        if(l[i]<l[j]):
            pass 
        else:
            t=l[i]
            l[i]=l[j]
            l[j]=t 
print(l)
