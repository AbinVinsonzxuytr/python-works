result=lambda a:a**2
print("square=",result(5))

d={"name":"Abin",'age':12}
n=lambda a:a["name"]
print(n(d))

length=lambda a:len(a)
print("length of apple is",length("apple"))

first=lambda a:a[0]
print("first element of apple is",first("apple"))


last=lambda a:a[-1]
print("last element of apple is",last("apple"))

sum=lambda a,b:a+b
print(sum(2,3))

sum3=lambda a,b,c:a+b+c
print(sum3(2,3,4))

product=lambda a,b,c,d:a*b*c*d
print(product(2,3,4,5))


