print("Defina un numero")
def operacion(a,b):
    x=1
    for i in range(b):
        x=x*a
    return x
a = int(input("dijite primer numero"))
b = int(input("dijite segundo numero"))
result=operacion(a,b)
print(result)