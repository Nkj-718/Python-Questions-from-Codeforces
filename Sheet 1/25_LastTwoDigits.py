a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
result=(a*b*c*d)%100
print(f"{result:02d}")
