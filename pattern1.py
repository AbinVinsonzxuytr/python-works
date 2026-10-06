# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# 2
# 4 6
# 8 10 12
# 14 16 18 20
# k=2
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(5,0,-1):
#     for j in range(i+1,1,-1):
#         print(i,end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
for i in range(1,5):
    for j in range(i+1,1,-1):
        print(j-1,end=" ")
    print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# A
# B B
# C C C
# D D D D
# k=64
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(i+k),end=" ")
#     print()

# A
# B C
# D E F
# G H I J
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k+64),end=" ")
#         k=k+1
#     print()

# A
# A B
# A B C
# A B C D
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()

# l=[12,34,56,78,13,87,5]
# k=len(l)
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")

# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")
