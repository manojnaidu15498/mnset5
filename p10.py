z=int(input())
x='no'
y='yes'
def powof2(n):
    if (n == 0):
        return x
    while (n != 1):
            if (n % 2 != 0):
                return x
            n = n // 2
             
    return y
print(powof2(z))    
