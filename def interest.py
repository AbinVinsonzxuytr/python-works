# # Define a function that takes 3 arguments (amount,rate,year) and find the simple interest value
# # si=(p*n*r)/100
#
# def simple(amount,rate,year):
#     si=0
#     si=(amount*rate*year)/1004
#     return si
# a=int(input("Enter Amount:"))
# b=int(input("Enter Rate:"))
# c=int(input("Enter Year:"))
# result=simple(a,b,c)
# print(result)


# def product(a,b,c):
#     return a*b*c
# e=int(input("Enter 1st the value :"))
# f=int(input("Enter the 2nd value :"))
# g=int(input("Enter the 3rd value :"))
# s=product(e,f,g)
# print(s)

# def occ(s,c):
#     count = 0
#     for i in s:
#         if i==c:
#             count=count+1
#     return count
# a=input("Enter the string :")
# b=input("Enter the character :")
# h=occ(a,b)
# print("The occurence of ",b, "in ",a, "is ",h)

# # Define a function that takes a list as argument and returns a new list containing unique elements
# j=[23,34,78,12,67,34,90,23]
# def unique(l):
#     k=[]
#     for i in l:
#         if i not in k:
#             k.append(i)
#     return k
# u=unique(j)
# print(u)


# # Define the function that takes arguments as two lists and print the common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def common(a,b):
#     for i in a:
#         if i in b:
#             print(i)
# common(list1,list2)

# def fun(n,a=9999):
#     print('NAME',n)
#     print('AGE',a)
# fun("Abin")


# def funs(*args):
#     print(args)
# funs(1,2,3,4,5,6)

# def fun(**kwargs):
#     print(kwargs)
# fun(name='Abin',age="23")


# Define a function that accepts any numbers of numbers that returns their sum
# def sum(*suiii):
#     sum=0
#     for i in suiii:
#         sum=sum+i
#     print(sum)
# sum(1,2,3,4,5,6)
