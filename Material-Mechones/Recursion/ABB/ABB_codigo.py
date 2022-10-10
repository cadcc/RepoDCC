### Código ABB

'''
Antes de crear la recursión del ABB, debemos tener una estructura que lo defina 
(te recomendamos ver las cápsulas de clases en python si no sabes utilziar clases en python)

'''

class Arbol:
    def __init__(self, raiz = None, izq = None, der = None):
        self.izq = izq
        self.raiz = raiz
        self.der = der

    # Retorna el mayor elemento de un árbol
    def mayor(self):
        if self.der == None: return self.raiz
        return self.der.mayor()
    
    # Retorna el menor elemento de un árbol
    def menor(self):
        if self.izq == None: return self.raiz
        return self.izq.menor()
    
    def isABB(self):
        v = self.raiz
        if v == None:
            return True
        p = (self.izq ==None) or self.izq.mayor() < v and self.izq.isABB()
        q = (self.der ==None) or self.der.menor() > v and self.der.isABB()
        return p and q

# Ejemplo de inicialización
'''
Notar que si no se especifica elvalor de raiz, izq o der, la clase se 
inicializa con estos parámetros igual a None
'''
ABB1 = Arbol(
    10,
    Arbol(5, Arbol(3), Arbol(6)),
    Arbol(12, Arbol(11))
)

AB1 = Arbol(
    10,
    Arbol(12, Arbol(11)),
    Arbol(5, Arbol(3), Arbol(6))
)


assert ABB1.isABB()
assert not AB1.isABB()


### Printeo en orden ###
'''
Para hacer el print en orden basta con recorrer primero todo los nodos izquierdos del árbol,
luego pasar por la raiz y terminamos con el lado derecho
'''
# ABB_Orden: ABB -> None
# Entrega los nodos del arbol ordenados
def ABB_Orden(ABB):
    if ABB == None: return
    # Nos aseguramos de que es ABB
    ABB.isABB()

    # Recorremos los nodos izquierdos
    ABB_Orden(ABB.izq)

    # Printeamos el valor céntrico
    print(ABB.raiz)

    # Recorremos los nodos derechos
    ABB_Orden(ABB.der)

# ABB_Orden(ABB1)

### Otras formas posibles de ordenar:
'''
    preorden : primero vemos la raiz, luego el subárbol izquierdo y finalmente el derecho
    postorden : primero vemos el sub arbol izquierdo, luego el derecho y finalmente la raiz
'''
# ABB_Orden: ABB -> None
# Entrega los nodos del arbol en formato preorden
def ABB_Preorden(ABB):
    if ABB == None: return
    # Nos aseguramos de que es ABB
    ABB.isABB()

    # Printeamos el valor céntrico
    print(ABB.raiz)

    # Recorremos los nodos izquierdos
    ABB_Preorden(ABB.izq)

    # Recorremos los nodos derechos
    ABB_Preorden(ABB.der)

#ABB_Preorden(ABB1)

# ABB_Orden: ABB -> None
# Entrega los nodos del arbol en formato postorden
def ABB_Postorden(ABB):
    if ABB == None: return
    # Nos aseguramos de que es ABB
    ABB.isABB()

    # Recorremos los nodos izquierdos
    ABB_Postorden(ABB.izq)

    # Recorremos los nodos derechos
    ABB_Postorden(ABB.der)

    # Printeamos el valor céntrico
    print(ABB.raiz)

#ABB_Postorden(ABB1)

'''
Notar que la noción que podemos encontrar en estas formas de recorrer el árbol es que
la recursión se queda 'esperando'. Por ejemplo, cuando recorremos por orden, y llamamos
por primera vez a ABB_orden(ABB1), no printeamos el valor de la raiz de ABB1 hasta que 
la recursión ABB_orden(ABB1.izq) retorna.
''' 