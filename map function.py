l=[1,2,3,4,5]
result=list(map(lambda x:x**2,l))
print(result)

print(set(map(lambda x:x**2,l)))

result=tuple(map(lambda x:x**2,l))
print(result)

print(list(map(lambda x:x**3,l)))

print(list(map(lambda x:x**0.5,l)))

l1=['red','green','blue','yellow','black']
print(list(map(lambda x:len(x),l1)))
print(list(map(lambda x:x[0],l1)))
print(list(map(lambda x:x[-1],l1)))
print(list(map(lambda x:x[::-1],l1)))

l=[23,78,12,56]
print(list(map(lambda x:x+10,l)))

##given a list of dictionaries
l=[{'emp_id':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
{'emp_id':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
{'emp_id':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# create a new list of emails
print(list(map(lambda x:x['email'],l)))