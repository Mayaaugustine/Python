#Given a list of unique numbers, swap the minimal and maximal elements of this list.
# Print the resulting list.
a = [10,30,50,100,60,190,5650,5560,6985,4567,500]
x= len(a)
b=[]
c=[]
b=a.copy()
a.sort()
print(a)
print(b)

for i in range (0,len(b)):
  print(b[i])