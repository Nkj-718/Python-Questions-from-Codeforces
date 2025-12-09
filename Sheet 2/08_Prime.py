x=int(input())
check=False
for i in range(2,x):
    if(x%i==0):
        check=True
        break
if(check==True):
    print("NO")
else:
    print("YES")