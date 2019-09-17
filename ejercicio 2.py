print("Defina un numero")

def operacion(a,b):
    x=1
    for i in range(b):
        x=x*a
    return x


a = int(input("dijite primer numero"))
b = int(input("dijite exponente"))
result=operacion(a,b)
print(result)
v = int(input("dijite segundo numero"))
n = int(input("dijite exponencial"))
result2=operacion(v,n)
if result>result2:
    print("el primer resultado es mayor al segundo")
else:
    print("el segundo numero es mayor al primero")