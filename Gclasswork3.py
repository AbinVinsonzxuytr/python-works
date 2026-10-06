# #Write a program to check whether two entered numbers are equal or not


n = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
if n == n2:
    print("Both are equal")
else:
    print("The numbers are not equal")

# #Write a program to check whether two entered words are equal or not

n0 = str(input("Enter the words: "))
n1 = str(input("Enter the words: "))
if n0 == n1:
    print("Both are equal")
else:
    print("The words are not equal")

# #Write a program to find the maximum of two numbers

n4 = int(input("Enter the number: "))
n5 = int(input("Enter the number: "))
if n4 < n5:
    print(n5, "is maximum")
else:
    print(n4, "is maximum")

# #write a program to check whether the entered character is vowel or not

l1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
n6 = str(input("Enter the character: "))
if n6 in l1:
    print(n6, "is a vowel")
else:

    print(n6, "is not a vowel")

# #Write a program to check whether the entered country name contains word 'land'

n7 = (input("Enter the word: "))
if 'land' in n7:
    print("word contain land")
else:
    print("word not contain land")

# #write a program to check whether the entered number is 3 digit or not

n8 = int(input("Enter the number: "))
n9 = str(n8)
if len(n9) == 3:
    print(n9, "is a 3-Digit number")
else:
    print(n9, "is not a 3-Digit number")

# write a program to check whether the entered string is  palindrome or not

n10 = str(input("Enter the string: "))
if (n10[::-1] == n10):
    print(n10, "is a palindrome string")
else:
    print(n10, "is not a palindrome string")
# Write a program to check whether a number is present in given list

l = [23, 67, 12, 90]
n11 = int(input("Enter the number: "))
if n11 in l:
    print(n11, "is present in the list")
else:
    print(n11, "is not present in the list")

# Write a program to check whether a key is present in a dictionary or not
d = {101: 'Arun', 102: 'Amal', 103: 'Anu'}

n12 = int(input("Enter the key: "))
if n12 in d:
    print(n12, "is present in the dictionary")
else:
    print(n12, "is not present in the dictionary")

#Write a program to check whether the given password is strong/weak(if length less than 8 weak)

n13=(input("Enter the password: "))
if len(n13)>=8:
    print(n13,"is strong password")
else:
    print(n13,"is not a strong password")