num1,num2=map(int,input().split())
while(num1>0 and num2>0):
    i1=min(num1,num2)
    i2=max(num1,num2)
    sum=0
    for i in range(i1,i2+1):
        print(i, end=' ')
        sum=sum+i
    print(f"sum ={sum}")
    num1,num2=map(int,input().split())