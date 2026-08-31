L=[1,3,4,1,2,1,2,7,8,5,3,1]
D={}
for i in L:
    count=0
    for j in L:
        if i==j:
            count+=1
    D[i]=[count]        
print(D)        
