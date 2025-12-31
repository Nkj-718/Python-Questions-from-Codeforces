n=int(input())
for i in range(1,n+1):
    right=i-1
    space=" "*(n-i)
    stars="*"*(i+right)
    print(f"{space}{stars}")