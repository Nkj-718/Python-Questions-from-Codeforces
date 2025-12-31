n,a,b=map(int,input().split())
sum=0
for i in range(1,n+1):
    num=str(i)
    value=0
    for j in num:
        value=value+int(j)
    if(a<=value<=b):
        sum=sum+i
print(sum)