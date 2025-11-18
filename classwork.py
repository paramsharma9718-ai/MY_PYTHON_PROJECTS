def char_freq(n):
    d={}
    a=[]
    for i in range(len(n)):
        x=n.count(n[i])
        a.append(x)
        d[n[i]]=a[i]
    return d

n=input("ENTER SENTENCE")    
result=char_freq(n)
print(result)