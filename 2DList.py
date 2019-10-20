# a=[[1,2,3],[1,2]]
# m=4
# n=4
# a=[]
# for i in range (n):
#     a.append([0]*m)
#
# print(a)
#
# ## sequence generator
#

a=[[0,0,0],[0,0,0],[0,0,0]]
x= len(a)
y=x

for i in range(x):
    for j in range(x):
        if i==j:
            a[i][j] = 1
        elif i<j:
            a[i][j] = 0
        else:
            a[i][j] = 2

print(a)