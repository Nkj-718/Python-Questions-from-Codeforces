Range=int(input())
print("2", end=' ')
for i in range(3,Range+1):
    check=False
    for j in range(2,i):
        if(i%j==0):
            check=True
            break
    if(check!=True):
        print(i, end=' ')