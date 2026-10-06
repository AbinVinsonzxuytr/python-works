# def add():
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     sum=num1+num2
#     print(sum)
#     return
# add()

def name():
    n=input("enter your name:")
    print('Hello '+n)
    return
name()

def fact():
    s=1
    n=int(input("Enter the number:"))
    for i in range(1,n+1):
        s=s*i
    print(s)
fact()

def occ():
    count=0
    n=input("Enter the string:")
    k=input("Enter the character :")
    for i in n:
        if i==k:
            count=count+1
    print(count)
occ()

def list_add():
    sum=0
    l=[89,45,67,12]
    for i in l:
        sum=sum+i
    print(sum)
list_add()