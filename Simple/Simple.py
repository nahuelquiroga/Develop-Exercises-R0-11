import random
import doctest

def generadora_lista():
    lista_desordenada = [{'id' : 0 , 'edad' : random.randint(1,100)},
                         {'id' : 1 , 'edad' : random.randint(1,100)},
                         {'id' : 2 , 'edad' : random.randint(1,100)},
                         {'id' : 3 , 'edad' : random.randint(1,100)},
                         {'id' : 4 , 'edad' : random.randint(1,100)},
                         {'id' : 5 , 'edad' : random.randint(1,100)},
                         {'id' : 6 , 'edad' : random.randint(1,100)},
                         {'id' : 7 , 'edad' : random.randint(1,100)},
                         {'id' : 8 , 'edad' : random.randint(1,100)},
                         {'id' : 9 , 'edad' : random.randint(1,100)}]
    
    return lista_desordenada

def ordenadora():
    
    lista_ordenada = generadora_lista()
    lista_ordenada.sort(key=lambda l: l['edad'],reverse=True)
    print(lista_ordenada[-1]['id'])
    print(lista_ordenada[0]['id'])

    return lista_ordenada

