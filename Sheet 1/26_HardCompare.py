import math
a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
val1=b*math.log(a)
val2=d*math.log(c)
if(val1>val2):
    print("Yes")
else:
    print("No")