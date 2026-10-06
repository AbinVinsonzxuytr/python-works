l=[1,2,3,4]
new={i:i**2 for i in l}
print(new)

new1={i:l[i] for i in range(len(l))}
print(new1)

s='python coding is easy and fun'
new2={i:len(i) for i in s.split()}
print(new2)