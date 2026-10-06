#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *
j=2
for i in range(0,4):
    for j in range(0,j+1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end="   ")
    j=j-1
    print()
j=0
for i in range(3,0,-1):
    for j in range(0,j+1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end="   ")
    j=j+1
    print()


#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#           *  *
#           *  *
#        *  *  *  *
#        *  *  *  *
#     *  *  *  *  *  *
#     *  *  *  *  *  *
#  *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *
j=8
for i in range(0,9,2):
    for l in range(2):
        for j in range(1,j+1):
            print("",end="  ")
        for k in range(1,i+1):
            print("*",end="   ")
        print()
    j=j-2