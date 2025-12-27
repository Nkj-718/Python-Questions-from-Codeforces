t=int(input())
for i in range(0,t):
    num=input()
    rev=num[::-1]
    for j in rev:
        print(j, end=' ')
    print()