
# # #create a new list with square root of each element
# # l=[25,16,9,36]
l=[25,16,9,36]
k=[i**.5 for i in l]
print(k)

# #Given a dictionary
d={'Arun':25,'Amal':34,'Akhil':26,'Anu':21}
# # create a list of names
# # create a list of marks
l1=[i for i in d]
print(l1)
l2=[i for i in d.values()]
print(l2)

# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# #create a list of string values
# #create a list of floats
# #create a list of positive number
l3=[i for i in l if i==str(i)]
print(l3)
l4=[i for i in l if type(i)==float]
print(l4)
l5=[i for i in l if (type(i)==int or type(i)==float) and i>0]
print(l5)

# #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
# #create a new list with elements whose value is divisible by 3 in range(1,101)
l6=[i for i in fruits if len(i)>6]
print(l6)
l7=[i for i in range(1,101) if i%3==0]
print(l7)
# Given
s="python coding is easy and fun"
# # create a new list with only vowels
l8=['a','e','i','o','u']
l9=[i for i in s if i in l8]
print(l9)