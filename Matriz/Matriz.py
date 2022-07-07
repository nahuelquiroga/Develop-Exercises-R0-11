import numpy as np 

consecutivo = 0
array = np.random.randint(25, size=(5, 5))
print(array)

### TEST MATRIZ DE ENTRADA

# array = np.empty((0, 5), int)
# array = np.append(array, np.array([[ 10 , 24 , 15 , 5 , 13 ]]), axis=0)
# array = np.append(array, np.array([[ 9  , 22 , 23 , 2 , 14 ]]), axis=0)
# array = np.append(array, np.array([[ 8  , 1  , 2  , 3 , 4  ]]), axis=0)
# array = np.append(array, np.array([[ 7  , 6  , 7  , 4 , 12 ]]), axis=0)
# array = np.append(array, np.array([[ 16 , 19 , 5  , 5 , 21 ]]), axis=0)

for x in range(0,5):
    fila = array[x,:]
    for y in range(0,4):
        if ( fila[y] - fila[y+1] == 1 or fila[y] - fila[y+1] == -1 ):
            consecutivo = consecutivo +1
        else:
            consecutivo = 0
        if  consecutivo == 3 :
            print("La posición del elemento inicial es [" + str(x) + "," + str(y-2) + "] es decir fila: " + str(x+1) + " columna: " + str(y-1))
            print("La posición del elemento final es [" + str(x) + "," + str(y+1) + "] es decir fila: " + str(x+1) + " columna: " + str(y+2))
            consecutivo = 0
        else:
            pass
        
for x in range(0,5):
    columna = array[:,x]
    for y in range(0,4):
        if ( columna[y] - columna[y+1] == 1 or columna[y] - columna[y+1] == -1 ):
            consecutivo = consecutivo +1
        else:
            consecutivo = 0
        if  consecutivo == 3 :
            print("La posición del elemento inicial es [" + str(y-2) + "," + str(x) + "] es decir fila: " + str(y-1) + " columna: " + str(x+1))
            print("La posición del elemento final es [" + str(y+1) + "," + str(x) + "] es decir fila: " + str(y+2) + " columna: " + str(x+1))
            consecutivo = 0
        else:
            pass
