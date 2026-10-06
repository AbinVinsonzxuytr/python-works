# 1
# 4 9
# 16 25 36
# 49 64 81 100
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k**2,end=" ")
        k=k+1
    print()

# 1
# 3 3 3
# 5 5 5 5 5
for i in range(1,6,2):
    for j in range(1,1+i):
        print(i,end=" ")
    print()

# 1
# 1A1
# 1A1A1
for i in range(1,8,2):
    for j in range(1,i+1):
        if j%2==0:
            print("A",end=" ")
        else:
            print("1",end=" ")
    print()

#       *
#     *   *
#   *   *   *
# *   *   *   *
j=3
for i in range(1,5):
    for j in range(1,j+1):
        print(" ",end=" ")
    j=j-1
    for k in range(1,i+1):
        print("*",end="   ")
    print()

#      5
#     5   5
#   5   5   5
# 5   5   5   5

j=3
for i in range(1,5):
    for j in range(1,j+1):
        print(" ",end=" ")
    j=j-1
    for k in range(1,i+1):
        print("5",end="   ")
    print()

 # *   *   *   *
 #   *   *   *
 #     *   *
 #       *
j=0
for i in range(5,1,-1):
    for j in range(1,j+1):
        print("",end=" ")
    j=j+2
    for k in range(1,i):
        print("*",end="   ")
    print()

#           *  *
#           *  *
#        *  *  *  *
#        *  *  *  *
#     *  *  *  *  *  *
#     *  *  *  *  *  *
#  *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *


#        *
#      *   *
#    *   *   *
#  *   *   *   *
#    *   *   *
#      *   *
#        *

#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *
l=['red','green','blue','orange']
p=[i[0] for i in l]
print(p)