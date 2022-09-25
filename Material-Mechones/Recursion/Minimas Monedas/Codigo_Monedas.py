### Código menor cantidad de monedas
import sys

## min_coins: int list[int*] -> int
## Devuelve el numero minimo de monedas a utilizar
## min_coins(30, [10, 20, 30]) devuelve 1

def min_coins(k, list_coins):
    # Caso: nuestro k se vuelve 0
    if k == 0:
        return 0

    # nota: seteamos el minimo de monedas como un numero muy grande
    # a medidas que vayamos recorriendo list_coins, este valor bajará
    initial_coins = sys.maxsize

    # recorremos toda la lista con los distintos tipo de monedas
    for i in range(len(list_coins)):

            # Tomamo el valor i-ésimo de la lista y lo consideramos
            # como posible solución, calculamos el numero de monedas
            # necesarias para formar el valor de la resta entre k y
            # el valor i-ésimo en caso de que la resta no nos de negativo

            # nota: la resta no puede ser negativa dado que si así fuese
            # estaríamos hallando un k mayor al solicitado
        if k - list_coins[i] >= 0:
            aux_number = min_coins(k - list_coins[i], list_coins) + 1
    
        if aux_number != sys.maxsize:
            # Entonces sacamos el mínimo entre el valor de initial_coins
            # guardado en alguna recursión anterior, o el valor de 
            # considerar la moneda í-esima (aux_number)
            initial_coins = aux_number
    
    return initial_coins

# Pruebe la funcion:
print(min_coins(100, [10,20,30]))

# Note que se probamos con un valor más grande el compputador explota:
sys.setrecursionlimit(100000)

#print(min_coins(300, [10,20,30]))

'''
Esto se debe a la cantidad de iteraciones que debe realizar el programa, 
como vimos en el video, hay valores que se repiten constantemente, 
para esto, es mejor comenzar desde 'abajo hacia arriba'. Para esto,
comenzaremos de un k muy bajo, he iremos subiendo el valor del k hasta
llegar al valor deseado. La gracia de esta metodología es que cuando vayamos
incrementando el valor de nuestro k iremos almacenando el numero minimo
de monedas para formar dicho valor, con lo que cuando lleguemos al k
deseado ya tendremos su valor de mínimas monedas C:
'''
# min_coins_mem: int list[int] -> int
# Entrega el numero minimo de monedeas para formar
# un valor k (utiliza memoria)
def min_coins_mem(k, list_coins):
    # Lista que irá almacenando nuestro valores de monedas minimos
    list_vals = [0] * (k + 1)

    for i in range(1, k + 1):

        # Analogo a la funcion anterior, seteamos un valor máximo
        # como el minimo de monedas (a priori) para cada iteracion
        list_vals[i] = sys.maxsize

        # Recorremos la lista de monedas
        for coin in range(len(list_coins)):

            # Evitamos volver el k negativo
            if i - list_coins[coin] >= 0:
                # Guardamos el resultado como el número de monedas
                # para obtener el valor i - list_coins[coin], luego
                # le sumamos 1 por la moneda que estamos considerando
                # agregar (list_coins[coin])
                result = list_vals[i - list_coins[coin]] + 1

                # Actualizamos el valor en caso de que sea consistente
                # es decir, no tenga un valor maxsize
                if result != sys.maxsize:
                    list_vals[i] = result
    
    return list_vals[k]


# Notar que ahora estos casos son muucho más rápidos        
print(min_coins_mem(1000, [10,20,30]))