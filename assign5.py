#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.).
#Print the resulting list. If a list has an odd number of elements, leave the last element in place.

a = [10,30,50,100,60,190,5650,5560,6000]
x= len(a)
b=[]

z=x%2
print(z)
for i in range(0,x-1,2) :
    b.append(a[i+1])
    b.append(a[i])
    print(i)
    if x%2 > 0:
        print(i,x)
        if i>x:
            b.append(a[x-1])

print(b)