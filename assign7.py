# Given a list of numbers, find and print the elements that appear in the list only once.
# The elements must be printed in the order in which they occur in the original list.
a = [10,30,50,100,60,190,5650,5560,6985,4567,500,10,500,60,5560]
x= len(a)
b=[]
c=[]
b=a.copy()

for i in range (0,x):
    if a.count(a[i])==1:
        c.append(a[i])
print(c)

