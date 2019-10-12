
###Determine the number of even elements in the sequence ending with the number 0.

a = [10,11,12,30,14,50,100,60,57645,190,5650,55650,600]
b = len(a)
for i in range(0,b) :
    if a[i]%10 == 0:
        print(a[i])

