# Q.Write Python Programs Using map(), filter(), or reduce()
# 1.Capitalize all names in a list
names = ['alin', 'arun', 'anu']
print(list(map(lambda x:x.capitalize(),names)))

# 2.Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
print(list(map(lambda x:x+"@gmai.com",users)))

# 3.Filter out all empty strings from a list
words = ['hello', ' ', 'world', ' ', 'python']
print(list(filter(lambda x:x!=' ',words)))


# 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(list(filter(lambda x:x[0]=='A',names)))

# 5.Concatenate all strings in a list
words = ['Python', 'is', 'fun']
import functools
print(functools.reduce(lambda x,y:x+y,words,''))

# 6.Multiply all numbers in a list
nums = [2, 3, 4]
import functools
print(functools.reduce(lambda x,y:x*y,nums,1))

# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
print(list(map(lambda x:x[0],words)))

# 8.Add 10 to Each Number
nums1 = [5, 10, 15]
import functools
print(functools.reduce(lambda x,y:x+y,nums1,0))

# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
    # #Sum of Positive Odd numbers
    # #Sum of Negative  odd numbers
    # #Sum of Negative Even numbers
    # #Count of Positive numbers
    # #Count of negative numbers
l1=(list(filter(lambda x:x%2==0 and x>=0,l)))
import functools
print("Sum of positive even no :",functools.reduce(lambda x,y:x+y,l1,0))
l2=(list(filter(lambda x:x%2==1 and x>=0,l)))
import functools
print("Sum of positive odd no :",functools.reduce(lambda x,y:x+y,l2,0))
l3=(list(filter(lambda x:x%2==1 and x<=0,l)))
import functools
print("Sum of negative odd no :",functools.reduce(lambda x,y:x+y,l3,0))
l4=(list(filter(lambda x:x%2==0 and x<=0,l)))
import functools
print("Sum of negative even no :",functools.reduce(lambda x,y:x+y,l4,0))
l5=list(filter(lambda x:x>=0,l))
print("Length of positive no :",len(l5))
l6=list(filter(lambda x:x<=0,l))
print("Length of negative no :",len(l6))

# 10.Given a list
nums2 = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
print(list(map(lambda x:int(x),nums2)))

# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
l3=list(map(lambda x:x['name'],p))
print(list(map(lambda x:x.upper(),l3)))

#print products with price greater than 10000
l4=list(map(lambda x:x['price'],p))
print(list(filter(lambda x:x>10000,l4)))

#Find the total price of all products
import functools
print("Total price :",functools.reduce(lambda x,y:x+y,l4,0))