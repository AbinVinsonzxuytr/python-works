s="python coding is easy and fun"
new={i for i in s if i!=' '}
print(new)

new1={i for i in s if i in 'aeiou'}
print(new1)

new2=[len(i) for i in s.split()]
print(new2)