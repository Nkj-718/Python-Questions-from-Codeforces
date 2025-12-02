n=int(input())
for i in range(1,n+1):
    if(n>=2 and (i%2)==0):
        print(i)
    elif(n<2):
        print("-1")