#Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors.
a = [100,30,50,100,60,190,5650,55650,600]
b = len(a)
count=0
for i in range(0,b-1) :
    if a[i+1] > a[i]:
         if a[i + 1] > a[i+2]:
            print(a[i+1])