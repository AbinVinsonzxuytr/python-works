h="hello world"
d={}
count=0
for i in h:
    if i==" ":
        continue
    if i in d:
        count+=1
    else:
        d[i]=1
print(d)