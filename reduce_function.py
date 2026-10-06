import functools
# sum of list
l=[1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b,l,0))
# product of list
print(functools.reduce(lambda a,b:a*b,l,1))
