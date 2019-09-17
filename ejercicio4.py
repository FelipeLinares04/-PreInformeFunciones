def primo(a):
    num=0
    mitadE=(a+1)//2
    for i in range(1, mitadE+1):
        if (a+1)%i==0:
            num=num+1


    if num<2 and a%6!=0:
        print("es un primo hermano")
    else:
        print("no es primo hermano") 

x=int(input("El numero a probar es: "))
primo hermano(x)