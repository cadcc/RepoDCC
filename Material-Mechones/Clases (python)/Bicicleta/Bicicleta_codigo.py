'''
Video clases en python disponible en el link
link[]
'''
import math as m

## Primera implementación
class Engranajes1:
    def __init__(self, engPedal, engRueda):
        self.engPedal = engPedal
        self.engRueda = engRueda

    '''
    Metodo que nos calcula la relacion
    de la clase rueda
    '''
    def relacion(self):
        return self.engPedal / self.engRueda


## Segunda implementación
class Engranajes2:
    def __init__(self, engPedal, engRueda, groLlanta, diaRueda):
        self.engPedal = engPedal
        self.engRueda = engRueda
        # Se agregan nuevo parámetros
        self.groLLanta = groLlanta
        self.diaRueda = diaRueda
    
    def relacion(self):
        return self.engPedal / self.engRueda

    '''
    Método que retorna la circunferencia
    de la llanta
    '''
    def circunferencia(self):
        return (self.groLLanta * 2 + self.diaRueda) * m.pi

    '''
    Método que nos indica la distancia por
    cada pedaleada
    '''
    def avance(self):
        return self.circunferencia() * self.relacion()


## Tercera implementaciín (y la que consideramos correcta)
'''
Esta implementación se caracteriza porque presenta un trabajo 
abstracto de separación de clases o 'delegación' de trabajos.
Ahora las características de la rueda no pertenecen al engranaje
de la bicicleta, sino que es una clase por sí misma. 
'''

# Primero definimos la clase rueda
class Rueda:
    def __init__(self, groLlanta, diaRueda):
        self.groLlanta = groLlanta
        self.diaRueda = diaRueda

    def circunferencia(self):
        return (self.groLlanta * 2 + self.diaRueda) * m.pi

# Definimos la nueva clase engranaje, notar que
# uno de los parámetros es la clase Rueda (ruedaTrasera)
class Engranajes:
    def __init__(self, engPedal, engRueda, ruedaTrasera):
        self.engPedal = engPedal
        self.engRueda = engRueda
        # Objeto de la clase Rueda
        self.ruedaTrasera = ruedaTrasera

    def relacion(self):
        return self.engPedal / self.engRueda
    
    def avance(self):
        # Dado que RuedaTrasera es un objeto de clase Rueda,
        # podemos ocupar su método Circunferencia
        return self.ruedaTrasera.circunferencia() * self.relacion()


## Pequeños Test de implementación ##

# Engranaje con la primera implementación
_Engranajes1 = Engranajes1(2, 3)

# Engranaje con la seguna implementación
_Engranajes2 = Engranajes2(2, 3, 2, 10)

# Engranaje con la tercera implementación
_ruedaAtras = Rueda(2, 10)
_Engranajes3 = Engranajes(2, 3, _ruedaAtras)

# El resultado debe ser el mismo, la función relación no cambia
assert _Engranajes1.relacion() == _Engranajes3.relacion()
assert _Engranajes2.relacion() == _Engranajes3.relacion()

# El método 'avance' debe entregar el mismo resultado para
# la 2da y 3ra implementación
assert _Engranajes2.avance() == _Engranajes3.avance()
