# # # # Write a program to find the position of a character in a string
# n=input("Enter the string")
# y=input("Enter the character")
# if y in n:
#     print(n.index(y))
# else:
#     print("String not found")


# # # write a program to find the count of character in  a string
# n=input("Enter the string")
# y=input("Enter the character")
# print(n.count(y))
#
# # # create a random 5 digit otp number and print otp number
# import random
# print(random.randint(10000,99999))
#
# # # create a list of  5 random 3-digit numbers
# import random
# k=[]
# for i in range(5):
#     i=(random.randint(100,999))
#     k.append(i)
# print(k)
#
#
# # # create a dictionary where keys are words and values are length of each word from the string
#
# s="python coding is easy and fun"
# l={i:len(i) for i in s.split()}
# print(l)
#
#
# # # create a dictionary where keys are each character and values are number of occurence of each character
# s="hello world"
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)
#
# # # write a program to find the number of digits,letters,and spaces in a string
# s="sdfghjk3456789  dffghjkl345678"
# count_alpha=0
# count_digit=0
# count_space=0
# for i in s:
#     if i.isalpha():
#         count_alpha+=1
#     elif i.isdigit():
#         count_digit+=1
#     elif i.isspace():
#         count_space+=1
#     else:
#         print("----INVALID STRING----")
# print("letters=",count_alpha)
# print("digits=",count_digit)
# print("spaces=",count_space)
#
#
# # # Given a list
# l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# # # create a list of salaries
# # # find the maximum salary
# # # find minimum salary
#
# k=[]
# for i in range(len(l)):
#     k.append(l[i][2])
# print("Salaries=",k)
# print("maximum salary=",max(k))
# print("minimum salary=",min(k))
#
#
#
#
# # #cGiven a dictionary
# d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
# # create a new list of students whose mark>=40
# l=[i for i in d.values() if i>=40]
# print(l)
#
# # # Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# # Find Common elements
# for i in l1:
#     if i in l2:
#         print(i)
#
#
# #Given
# l=[23,45,67,12,90,56]
#
# #find second-largest number
# #find second-smallest number
#
# l.sort()
# l.pop()
# print("Second largest=",l[-1])
# l.sort(reverse=True)
# l.pop()
# print("second smallest=",l[-1])