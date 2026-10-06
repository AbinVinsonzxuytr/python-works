num = str(input("Enter the number: "))
if len(num)==2:
    print(num, "is a 2 digit number")
elif len(num)==3:
    print(num, "is a 3 digit number")
elif len(num)==4:
    print(num, "is a 4 digit number")
else:
    print(num, "is not a 2,3,4 digit number")
    