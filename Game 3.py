import random
a= -1
b=random.randint(1,99)
c=1
z=99
while a!=k:
    print ("is your number ",b,"?")
    r=input()
    if r=="b":
        c=b
        b=random.randint(c,z)
    elif r=="k":
        z=b
        b=random.randint(c,b)
    elif r=="d":
        print("Yeaaaaay!!, your number is: ",b) 
        break
   
  

