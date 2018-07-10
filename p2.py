s1=input()
s2=input()
a=len(s1)
b=len(s2)
if a>b:
    print(s1)
elif a==b:
    print(s1 or s2)
else:
    print(s2)
