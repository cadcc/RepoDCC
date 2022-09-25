'''
Video clases en python disponible en el link
link[]
'''

# Ejemplo de SuperHeroes

class Heroe:
    def __init__(self, vida, mana, nombre):
        self.vida = vida
        self.mana = mana
        self.nombre = nombre
    
    '''
    Método que tiene el héroe para decir su 
    nombre, observe que no necesitamos más
    parámetros que el self, este debe ir en
    todos los métodos de una clase.
    '''
    def  decir_nombre(self):
        print("Mi nombre es " + self.nombre)

    '''
    Método para descansar, el héroe recupera
    vida y maná.
    '''
    def descansar(self):
        self.vida += 2
        self.mana += 2

    '''
    Método para comer, en este caso no nos 
    basta con solo considerar el self de
    nuestra clase, esto dado que estamos
    recibiendo un parámetro externo que no
    consideramos dentro de los atributos de
    nuestra clase.
    '''
    def comer(self, alimento):
        if alimento == 'Chokita':
            self.vida += 1
        if alimento == 'Sandwich':
            self.vida += 3

## Tests ##
batman = Heroe(10, 5, "Batman")

# Testeamos inicialización
assert batman.vida == 10
assert batman.mana == 5

# Testeamos método descansar
batman.descansar()
assert batman.vida == 12
assert batman.mana == 7

# Testeamos comer 'Chokita'
batman.comer("Chokita")
assert batman.vida == 13
assert batman.mana == 7

# Testeamos comer 'Sandwich'
batman.comer("Sandwich")
assert batman.vida == 16
assert batman.mana == 7

### Contenido EXTRA :D ###
'''
Si eres alguien que le apasiona los videojuegos
(no necesariamente pero necesito captar tu atención).
Probablemente te hayas dado cuenta de que no resulta 
lógico que el héroe al descansar recupere más
vida de la que tenía en un inicio.

Por ejemplo, batman comienza con 10 de vida y termina
con 16 (sin subir de nivel).

Existen varias formas de solucionar esta problématica,
la que veremos abajo consiste en tener dos parámetros
para la vida, uno de vida máxima y otro de vida actual
(identicamente para le maná). De esta forma, antes de
aumentar los valores, preguntaremos si no estamos 
infringiendo las características iniciales de nuestro 
personaje.
'''
class SuperHeroe:
    def __init__(self, vida, mana, nombre):
        
        self.nombre = nombre
        # Nuevas variables
        '''
        Es lógico que la vida actual del
        personaje sea la vida con la que
        es creado, la cual es a la vez la
        vida máxima
        '''
        self.vidaMaxima = vida
        self.vidaActual = vida

        self.manaMaximo = mana
        self.manaActual = mana

    '''
    Método para subir la vida de nuestro SuperHeroe
    recibe como parámetro self y el valor de vida
    que recupera el SuperHeroe
    '''
    def subir_vida(self, valor):
        # Si la vida actual más el valor es mayor
        # a la vida maximas, seteamos vida maxima
        if valor + self.vidaActual > self.vidaMaxima:
            self.vidaActual = self.vidaMaxima

        # Si no nos pasamos de la vida máxima,
        # Sumamos sin problemas
        else:
            self.vidaActual += valor

    '''
    Método para subir el maná de nuestro SuperHeroe
    recibe como parámetro self y el valor de vida
    que recupera el SuperHeroe
    '''
    def subir_mana(self, valor):
        if valor + self.manaActual > self.manaMaximo:
            self.manaActual = self.manaMaximo
        else:
            self.manaActual += valor

    '''
    Método con fines pedagógicos, le restamos vida
    y mana al SuperHeroe, notar que una correcta
    implementación del daño debería considerar
    que la vida y el  maná no pueden ser negativos.
    '''
    def dañar(self):
        self.vidaActual -=2
        self.manaActual -= 2

    def  decir_nombre(self):
        print("Mi nombre es " + self.nombre)

    def descansar(self):
        self.subir_vida(2)
        self.subir_mana(2)

    def comer(self, alimento):
        if alimento == 'Chokita':
            self.subir_vida(1)
        if alimento == 'Sandwich':
            self.subir_vida(3)

## Haremos unos pequeños tests ##

rorschach = SuperHeroe(10, 6, "Rorschach") # Es superHeroe¿?

# Testeamos inicialización
assert rorschach.vidaActual == 10
assert rorschach.vidaMaxima == 10
assert rorschach.manaActual == 6
assert rorschach.manaMaximo == 6

# Testeamos funcionamiento vida/mana maximos
rorschach.descansar()
assert rorschach.vidaActual == 10
assert rorschach.manaActual == 6

# Haremos Daño y luego curaremos
rorschach.dañar()
assert rorschach.vidaActual == 8
assert rorschach.manaActual == 4

rorschach.comer("Sandwich")
assert rorschach.vidaActual == 10
assert rorschach.manaActual == 4

'''
Como comentarios finales, notar que en caso de que
nuestro heroe sea capaz de subir de nivel, bastará
con tomar el valor vidaMaxima y manaMaximo y setearles
un valor más alto.
'''