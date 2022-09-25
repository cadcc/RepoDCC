from random import uniform

# Creamos la clase padre célula
class celula:               
    def __init__(self,size): 
        self.size = size

    '''
    Retorna el tamaño de
    la célula
    '''
    def get_size(self):
        return self.size


class procariot_cel(celula):
    '''
    Inicializamos la clase mediante
    el método super. Esto quiere decir
    que heredamos los métodos de
    celula. Le enviamos size dado
    que celula necesita un valor para
    poder inicializarse.
    '''
    def __init__(self,size):
        super().__init__(size)

    def get_type(self):
        return "Celula procariota"

    def where_is_info(self):
        return "La información está en el nucleoide"

    def wall_cel(self):
        return "No tiene pared celular" 

    def wall_cel(self):
        return "No tiene pared celular"


class eukariot_cel(celula):
    def __init__(self,size):
        super().__init__(size)

    def get_type(self):
        return "Celula eucariota"
    
    def where_is_info(self):
        return "La info está en el núcleo"

    '''
    A pesar de no tener definida la
    variable nucleo_size, los hijos
    si la tendrán, por ende no tenremos
    conflictos
    '''
    def get_nucleo_size(self):
        return self.nucleo_size

class animal_cel(eukariot_cel):
    def __init__(self,size):
        # Definimos el tamaño del nucleo
        # para la célula animal
        self.nucleo_size = 6

        # Heredamos de la clase eukariot_cel
        super().__init__(size)
        
    def get_type(self):
        '''
        super().get_tyupe() nos retorna solo
        el string Celula eucariota, nos basta
        con agregar el string animal
        '''
        resp = super().get_type() + " animal"
        return resp

    def esterol_kind(self):
        return "Colesterol"

    def wall_cel(self):
        return "No tiene pared celular"

class vegetal_cel(eukariot_cel):
    def __init__(self,size):
        # Definimos el tamaño del nucleo
        # para la célula animal
        self.nucleo_size = uniform(5,25.0)
        super().__init__(size)
    
    def get_type(self):
        resp = super().get_type() + " vegetal"
        return resp
    
    def esterol_kind(self):
        return "Fitoesterol"

    def wall_cel(self):
        return "Tiene pared celular"

class funji_cel(eukariot_cel):
    def __init__(self,size):
        # Definimos el tamaño del nucleo
        # para la célula animal
        self.nucleo_size = uniform(0.25,25.0)
        super().__init__(size)
    
    def get_type(self):
        resp = super().get_type() + " funji"
        return resp

    def esterol_kind(self):
        return "Ergoesterol"

    def wall_cel(self):
        return "Tiene pared celular"

### Tests ###
funji = funji_cel(3)
vegetal = vegetal_cel(4)
animal = animal_cel(5)
procariota = procariot_cel(2)

assert funji.get_type() == "Celula eucariota funji"
assert funji.nucleo_size > 0.25 and funji.nucleo_size < 25.0

assert vegetal.esterol_kind() == "Fitoesterol"
assert vegetal.nucleo_size > 5.0 and vegetal.nucleo_size < 25.0

assert animal.wall_cel() == "No tiene pared celular"
assert animal.nucleo_size == 6.0

assert procariota.get_size() == 2
assert procariota.where_is_info() == "La información está en el nucleoide"


'''
Nota: Puede darse la situación en que tengamos
métodos con el mismo nombre para el padre
y el hijo. En caso de que el uno de estos invoque dicho 
método, python comenzará a buscar por los
métodos de la clase que está llamando.
'''