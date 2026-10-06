a=int(input("Enter a number :"))
b=int(input("Enter another number :"))
op=input("Enter a operator :")
if op==("+"):
    print("Sum=",a+b)
elif op==("-"):
    print("Difference",a-b)
elif op==("*"):
    print('Product',a*b)
elif op==("/"):
    print("Division",a/b)
else:
    print("--------ERROR--------")