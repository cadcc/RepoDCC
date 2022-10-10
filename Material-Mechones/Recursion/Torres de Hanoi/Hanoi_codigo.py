### Códido Torres de Hanoi

## TorresHanoi: int -> int
## Entrega el número de movimientos para un n determinado
## TorresHanoi(3) -> 7

def TorresHanoi(n_discos):
    if n_discos == 1:
        return 1
    return TorresHanoi(n_discos - 1)*2 + 1

## Test
assert TorresHanoi(2) == 3
assert TorresHanoi(3) == 7
assert TorresHanoi(4) == 15

## Breve Explicación TorresHanoi:
'''
Como explicamos en el video, debemos mover todos los bloques (excepto el mayor)
para llegar de la estación 1 a la estación 2, para esto necvesitaremos los mismos
movimietnos que una torre de hanoi de n-1 discos. Luego movemos el n-ésimo disco
al pilar 3 (formando la tercera estación), es decir agregamos un documento.
Finalmente, movemos nuevamente todos los discos del pilar 2 al pilar 3
'''

## TorresHanoi2: int int int int -> None
## Nos muestra en pantalla los movimientos especificos para realizar
## un juego limpio de Torres de hanoi

def TorresHanoi2(n_discos, TorreInicio = 1, TorreAux = 2, TorreFin = 3):
    if n_discos == 1:
        print("Movemos de la Torre ", TorreInicio, " hacia la Torre ", TorreFin)
    else:
        TorresHanoi2(n_discos - 1, TorreInicio, TorreFin, TorreAux)
        print("Movemos de la Torre ", TorreInicio, " hacia la Torre ", TorreFin)
        TorresHanoi2(n_discos - 1, TorreAux, TorreInicio, TorreFin)
    return

## Prueba la funcion!!
TorresHanoi2(3)
