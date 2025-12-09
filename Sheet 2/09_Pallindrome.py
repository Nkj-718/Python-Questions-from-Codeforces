n=input()
reverse=n[::-1].lstrip('0')
print(reverse)
if(n==reverse):
    print("YES")
else:
    print("NO")