a=int(input())
l=list()
i=0
for i in range(a):
    x=int(input())
    l.append(x)
low=min(l)
hig=max(l)
print(low,hig)
