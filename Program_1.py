t=eval(input())
b=[min(t)]
a=min(t)[-1]
t.remove(min(t))
for i in t:
    for j in t:
        if a==j[0] and j[-1]!=b[0][0]:
            b.append(j)
            a=j[-1]
            t.remove(j)
            break
b=b+t
print(b)
