l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,l)))

# given a list
l=[23,67,90,12,45,52]
print(list(filter(lambda x:x>50,l)))

# given a list of fruits
f=['apple','orange','grape','pineapple','grapes']
print(list(filter(lambda x:len(x)>5,f)))

# given a list
l1=[34,78,96,23,12,15]
print(list(filter(lambda x:x%3==0 and x%5==0,l1)))
