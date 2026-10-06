# Q1.Define a function that takes 2 numbers and returns their product

def product(a,b):
    return a*b
k=int(input("Enter the number :"))
c=int(input("Enter the number :"))
l=product(k,c)
print(l)


# Q2.Define a function that takes a string and returns number of vowels
def vol(s):
    count=0
    l=['a','e','i','o','u']
    for i in s:
        for j in l:
            if i==j:
                count=count+1
    return count
k=input("Enter the string :")
print(vol(k))


# Q3.Define a function that takes length and breadth and returns area of rectangle

def area(l,b):
    e=l*b
    return e
k=int(input("Enter the length of the rectangle"))
m=int(input("Enter the breadth of the rectangle"))
areas=area(k,m)
print(areas)

# Q4.Define a function that takes a list of numbers and creates a new list with even numbers and returns the new list

def even(a):
    k=[]
    for i in a:
        if i%2==0:
            k.append(i)
    return k
l=[45,78,90,12,35]
p=even(l)
print(p)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# new=[6,12,3,21,8,17]

def digit(a):
    k=[]
    sum=0
    for i in a:
        for j in str(i):
            sum=sum+int(j)
        k.append(sum)
        sum=0
    return k
l=[123, 345, 111, 678, 134, 809]
p=digit(l)
print(p)