#Given a list of unique numbers, swap the minimal and maximal elements of this list.
# Print the resulting list.
a = [10,30,50,100,60,190,5650,5560,6985,4567,500]
x= len(a)
b=[]
c=[]
b=a.copy()
a.sort()
print(b)

for i in range (0,x-1):
  print(i)
  print(b[i])
  print(a[0])
  print(a[x-1])
  if a[0]==b[i]:
    c.append(a[x-1])
  elif a[x-1] == b[i]:
    c.append(a[0])
  else:
    c.append(b[i])

print(c)