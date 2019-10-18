#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.).
#Print the resulting list. If a list has an odd number of elements, leave the last element in place.
a = [10,30,50,100,60,190,5650,5560,6985,4567,500]
x= len(a)
b=[]
for i in range(0,x-1,2) :
    b.append(a[i+1])
    b.append(a[i])
if x%2 > 0:
    if x-1 > i:
        b.append(a[x-1])
print(b)