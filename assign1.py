##A sequence consists of integer numbers and ends with the number 0.
##Determine how many elements of this sequence are greater than their neighbors above.
a = [10,30,50,100,60,190,5650,55650,600]
b = len(a)
count=0
for i in range(0,b-1) :
     if a[i+1] > a[i]:
        print(a[i+1])


