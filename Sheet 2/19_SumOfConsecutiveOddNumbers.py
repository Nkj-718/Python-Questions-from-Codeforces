t=int(input())
for i in range(t):
    num1,num2=map(int,input().split())
    i1=min(num1,num2)
    i2=max(num1,num2)
    sum=0
    for j in range(i1+1,i2):
        if(j%2!=0):
            sum=sum+j
    print(sum)