f=int(input())
for i in range(1,f+1):
    n=int(input())
    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    print(fact)