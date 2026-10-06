

n = int(input("Enter the number OF CHOCOLATE: "))
j = n
total = 0
while n >= 3:
    new = n // 3
    rem = n % 3
    total += new
    n = new + rem

print(total + j)
print("rest packets",n)