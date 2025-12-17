symbol=input()
n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    for j in range(1,i+1):
        print(symbol, end='')
    print()