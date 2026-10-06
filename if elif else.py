a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
c=int(input("Enter the number 3: "))
if a>b>c:
    print(a,"is greater")
elif b>c>a:
    print(b,"is greater")
elif c>b>a:
    print(c,"is greater")
else:
    print("----ALL ARE EQUAL----")