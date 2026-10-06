#Given a list
colors=['red','green','blue','yellow','black','orange']
# #print each color
for i in colors:
    print(i)
# #print the first color starting with 'b'
for i in colors:
    if i[0]=='b':
        print(i)
#print all colors except color starting with 'b'
for i in colors:
    if i[0]=='b':
        continue
    print(i)
#print the first color contains letter 'n'
for i in colors:
    if i[0]=='n':
        print(i)
#print all colors except color contains letter 'n'

for i in colors:
    for j in i:
        if i=='n':
            continue
        print(i)
