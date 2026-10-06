#write a program to find BMI(Body Mass Index)

# BMI= weight in (kg)/ height**2 in (m)


# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

w=float(input("Enter weight in kg: "))
h=float(input("Enter height in m: "))
bmi=w/(h**2)
print(bmi)
if bmi<=18.4:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25 and bmi<=39.9:
    print("Overweight")
elif bmi>=40:
    print("Obedient")
else:
    print("--INVALID--")



#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.


n=int(input("Enter the order amount: "))
k=int(input("Enter the toy code: "))
if k==1:
    if n>1000:
        d=n-(n*10/100)
        print("The amount after 10% discount is ",d)
    else:
        print("No Discount")
elif k==2:
    if n>100:
        d=n-(n*5/100)
        print("The amount after 5% discount is ",d)
    else:
        print("No Discount")
elif k==3:
    if n>500:
        d=n-(n*10/100)
        print("The amount after 10% discount is ",d)
    else:
        print("No Discount")
else:
    print("Invalid code")

#3 FIZZBUZZ Problem
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
# otherwise -print the number

n=int(input("Enter a number: "))
if n%3==0:
    if n%5==0:
        print('fizzbuzz')
    else:
        print('fizz')
else:
    if n%5==0:
        print('buzz')
    else:
        print(n)