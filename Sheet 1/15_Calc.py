val=input()
lst=['+','-','*','/']
for s in lst:
    if s in val:
        a,b=val.split(s)
        a=int(a)
        b=int(b)
        if s=='+':
            print(a+b)
        elif s=='-':
            print(a-b)
        elif s=='*':
            print(a*b)
        elif s=='/':
            print(int(a/b))
        break