class Coche:
    # atributos
    rueda = 4
    color = ""
    aceleracion = 0
    velocidad = 0
    
    # Constructor
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
        
    # metodos
    def acelerar(self, velocidad=0):
        # self.velocidad = self.velocidad+self.aceleracion
        if velocidad > 0:
            self.velocidad += velocidad
        else:
            self.velocidad += self.aceleracion
            
        return self.velocidad

class autoVolador(Coche):
    ruedas = 6
    
    def __init__(self,color, aceleracion, esta_volando=False):
        super().__init__(color,aceleracion)
        self.esta_volando = esta_volando #atributos python

    def vuela(self):
        self.esta_volando = True
        return "estoy volando"
        
c1 = Coche('Rojo', 10)
print(c1.color)
print("------------------------------------------------")
cv1 = autoVolador('negro', 60)
print(cv1.color)
print(cv1.vuela())
print(cv1.esta_volando)

        