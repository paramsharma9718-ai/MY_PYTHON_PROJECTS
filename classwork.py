'''a=['apple','banana','cherry']
b=[]
for i in range(len(a)):
    c=len(a[i])
    b.append(c)
d=max(b)
t=b.index(d)
print(a[t])'''

def long_word(a):
    b=[]
    for i in range(len(a)):
        c=len(a[i])
        b.append(c)
    d=max(b)
    t=b.index(d)
    return a[t]



a=['apple','banana','cherry']
result=long_word(a)
print(f"LONGEST WORD IS : {result}")