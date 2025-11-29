a=input()
order=ord(a)
if(ord(a)>=65 and ord(a)<=90):
    order=order+32
    print(chr(order))
elif(ord(a)>=97 and ord(a)<=122):
    order=order-32
    print(chr(order))