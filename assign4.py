#Given a list of numbers, find and print all the elements that are greater than the previous element.
a = [10,30,50,100,60,190,5650,5560,6000]
b = len(a)
count=0
for i in range(0,b-1) :
    #print(a[i])
    if a[i+1] > a[i]:
        print(a[i+1])