def multiplicacion(a, b):
    print (f"La multiplicaicon de {a} y {b} es igual a: {a*b}")
    print (f"y el resultado de esta multiplicacion es: {par(a*b)}")
    
def par(a):
    if a % 2 == 0:
        return "par"
    else:
        return "Impar"
    
multiplicacion(3,5)
# print (f"el numero es: {par(3)}")