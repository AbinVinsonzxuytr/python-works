n=int(input("Enter a number :"))
if n%2==0:
    if n%3==0:
        print(n,"is divisible by 2 and 3")
    else:
        print(n,"is divisible by only 2 not 3")
elif n%3==0:
    print(n,"is divisible by only 3 not 2")
else:
    print(n,"is not divisible by 2 and 3")