n=1234
s=str(n)
for i in s:
    print(i)

l=[1,2,3,4]
sum=0
for u in l:
    sum=sum+u
print(sum)

dig=12345
s=str(dig)
sum=0
for i in s:
    sum=sum+int(i)
print(sum)

s='HELLO WORLD'
rev=""
for i in s:
        rev=i+rev
print(rev)

s=12345
rev=""
d=str(s)
for i in d:
    rev=i+rev
print(rev)

l=[1,2,3,4,5,6,7,8,9,10]
new=[]
for i in l:
    new.append(i*i)
print(new)


l=[1,2,3,4,5,6,7,8,9,10]
new={}
for i in l:
    new[i]=i**2
print(new)


s="hellow world"
for c in s:
    if c=="l":
        continue
    print(c,end=" ")

s="hellow world"
for c in s:
    if c=="l":
        break
    print(c,end=" ")