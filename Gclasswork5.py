# # #ARMSTRONG NUMBER
# sum=0
# for i in range(1,1000):
#     for j in str(i):
#         sum=sum+int(j)**len(str(i))
#     if sum==i:
#         print(i)
#     sum=0

# #Create new list with squares of each element
# l=[1,2,3,4]
# k=[]
# for i in l:
#     k.append(i**2)
# print(k)

# #Create a list with elements whose value is greater than 50
# l=[12,67,59,23]
# k=[]
# for i in l:
#     if i>50:
#         k.append(i)
# print(k)

# #Create a set with elements whose value is greater than 50
# l=[12,67,59,23]
# k=set()
# for i in l:
#     if i>50:
#         k.add(i)
# print(k)

# #Create a new dict where keys are numbers and values are squares of each numbers
# l=[1,2,3,4]
# k={}
# for i in l:
#     k[i]=i*i
# print(k)

#Create a list of 5 random numbers
# l=[]
# for i in range(5):
#     n=int(input("Enter a number:"))
#     l.append(n)
# print(l)

# #Find the factors of a number
# n=int(input("Enter number :"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# #Find the fibonacci series
# n=int(input('Enter the limit: '))
# a,b=0,1
# for i in range(n):
#     print(a)
#     a,b=b,a+b