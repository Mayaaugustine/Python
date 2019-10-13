# For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
# To do that, you can use the sep and end arguments for the function print()
print("please enter a number <=9")
n = int(input())
if n<=9:
    for i in range(0,n+1):
        for x in range(0,i):
            print(x+1,end='')
        print(end="\n")

else:
    print("error - please enter a number <=9")