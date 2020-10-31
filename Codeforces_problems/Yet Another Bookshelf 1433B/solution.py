#Yet Another Book Shelf

T=int(input()) # Taking Input


while T!=0 :
    n=int(input()) #input n
    v=[int(i) for i in  input().split()] # Taking array as input
    ind=[i for i in range(n) if v[i]==1]
    least=min(ind)
    most=max(ind)
    count=0
    for i in v[least:most]:
        if i==0:
            count+=1
    print(count)
    
    T-=1
