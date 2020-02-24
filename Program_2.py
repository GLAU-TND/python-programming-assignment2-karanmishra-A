t=eval(input())
t=[str(i) for i in t]
t.sort()
b=''
for i in range(len(t)-1):
    if t[i][0]==t[i+1][0] and len(t[i])<len(t[i+1]):
        a=t[i]
        t[i]=t[i+1]
        t[i+1]=a
for i in range(len(t)-1,-1,-1):
    b=b+t[i]
print(int(b))
