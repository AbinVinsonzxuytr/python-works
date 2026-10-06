# a=(input("Enter the month :"))
# if a=='January':
#     print(a," has 31 days")
# elif a=='February':
#     print(a," has 29 days")
# elif a=='March':
#     print(a," has 31 days")
# elif a=='April':
#     print(a," has 30 days")
# elif a=='May':
#     print(a," has 31 days")
# elif a=='June':
#     print(a," has 30 days")
# elif a=='July':
#     print(a," has 31 days")
# elif a=='August':
#     print(a," has 31 days")
# elif a=='September':
#     print(a," has 30 days")
# elif a=='October':
#     print(a," has 31 days")
# elif a=='November':
#     print(a," has 30 days")
# elif a=='December':
#     print(a," has 31 days")
# else:
#     print("-----ERROR-----")
month=(input("enter the month :"))
l1=['January','March','May','July','August','October','December']
l2=['April','June','September','November']
l3=['February']
if month in l1:
    print(month,"has 31 days")
elif month in l2:
    print(month,"has 30 days")
elif month in l3:
    print(month,"has 28 or 29 days")
else:
    print("-----ERROR-----")