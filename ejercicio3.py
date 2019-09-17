def divisor(a):
    num=0
    mitadE=a//2
    for i in range(1, mitadE+1):
        if a%i==0:
            num=num+1


    if num<2:
        print("el numero es primo")
    else:
        print("el numero no es primo") 

x=int(input("el resultado da: "))
divisor(x)