def divisor(a):
    z=1
    j=2
    for b in range(1,a+1):
        if(a%z==0):
            j=j+1
        z=z+1
    return j
print (divisor(672))
