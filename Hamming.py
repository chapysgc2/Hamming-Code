#Hazel Alain Garcia Lopez ---- Chapys
# Programa de Python 
# codigo hamming

#FUNCION PARA removerEspaciosR ESPACIOS DE LA CADENA
def removerEspacios(string):
    return "".join(string.split())
    
##########################################

def RedundanBits(m):
    # Usamos la formula 2 ^ r >= m + r + 1
    # calcular el numero de bits redundantes
    # Iterar sobre 0 .. m y devolver el valor
    # que satisface la ecuacion

    for i in range(m):
        if (2 ** i >= m + i + 1):
            return i

##FUNCION PARA LA REDUNDANCIA DE BITS#############################
def posRedundantBits(data, r):
    # Los bits de redundancia se colocan en las posiciones
    # que corresponden a la potencia de 2.
    j = 0
    k = 1
    m = len(data)
    res = ''

    #Si la posición es una potencia de 2, inserte '0'
    # De lo contrario, agregue los datos

    for i in range(1, m + r + 1):
        if (i == 2 ** j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1


    #El resultado se invierte ya que las posiciones son
    # contados hacia atras. (m + r + 1 ... 1)
    return res[::-1]

#################################################################

#FUNCION PARA DETECTAR ERRORES#######################################
def detectarERROR(arr, nr):
    n = len(arr)
    res = 0

    # Calcular bits de paridad de nuevo
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])

        # Crea un no binario agregando
        # bits de paridad juntos.

        res = res + val * (10 ** i)

    # Convertir de binario a decimal
    return int(str(res), 2)


####################################################################

#######FUNCION PARA LA PRIORIDAD DE BITS
def calcParityBits(arr, r):
    n = len(arr)

    # Para encontrar el bit de prioridad rth, iterar sobre
    # 0 a r - 1

    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # Si la posicion tiene 1 en un significativo
            # posicion, luego bit a bit O el valor de la matriz
            # para encontrar el valor del bit de paridad.

            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])
    
        # Concatenacion de cadenas
        # (0 a n - 2^r) + bit de paridad + (n - 2^r + 1 a n)
    
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

#########################################################################



#############ARRRANCA PROGRAMA SKRRRRR SKRRR



string = input("Ingrese palabra o texto:")
convertirPalabraBinario = ' '.join(format(c, 'b') for c in bytearray(string, "utf-8"))
print("El binario queda:", convertirPalabraBinario)




print("Quitamos los espacios")

#PROCESO PARA QUITAR LOS ESPACIOS
data = convertirPalabraBinario
string = convertirPalabraBinario
data1 = (removerEspacios(convertirPalabraBinario))
print(data1)

# Calcular el número de bits redundantes requeridos
m = len(data1) #cuenta los numeros de bits


r = RedundanBits(m) #Activa funcion y manda n bits para Calcular la redundancia

# Activa funcion para Determinar la posicion de la redundancia
arr = posRedundantBits(data1, r)

# Activa Funcion para determinar la prioridad de bits
arr = calcParityBits(arr, r)
cadenaNumero=len(arr)

# Transferimos los datos
print("Los datos transferidos y los que ocuparemos son:\n" + arr)
print("La cadena tiene", cadenaNumero , "bits")
print("Para que la simulacion de error, funcione")
print("debe cambiar un poco el valor por ejemplo")
print(
"10101001110 -> 11101001110, error en la posicion 10.  "
)
print("A continuacion se ingresara el error y debe ingresarlo con el tamaño igual :", cadenaNumero ," cambiando solo unos cuantos valores")
print(arr)
arrError = input("Ingrese error\n")
cadenaNumero2 = len(arrError)

# Simulamos el error en la transmisión cambiando un poco de valor.

if cadenaNumero == cadenaNumero2:

    arr = arrError
    print("Los datos de error son " + arr)
    correction = detectarERROR(arr, r)
    print("La posición de error es " + str(correction))

else:
    print("NO SE INGRESO BIEN LA CADENA")