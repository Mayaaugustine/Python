x=input()
y=input()
k=input()
a=int(x)
b=int(y)
c=int(k)
total=a*b

if total<c:
    print("no")
elif a%c==0  or b%c==0:
    print("Yes")
else:
    print("no")   