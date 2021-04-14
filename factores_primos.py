import time
import numpy
import random
import matplotlib.pyplot as plt

def factoresPrimos(num):

    primos = []
    inicio = time.time()
    for i in range(2,num + 1):

        while num % i == 0:
            primos.append(i)
            num = num / i
    fin = time.time()
    tiempo = float(fin - inicio)
    print("El tiempo de procesamiento fue:", tiempo)
    print(primos)
    return tiempo



def genNumbers():
    numbers = []
    for i in range(0,12):
        numbers.append(random.randint((10**i) , (10 ** (i+1)) ))
    return numbers


listNumbers = genNumbers()
listTime = []
for n in listNumbers:
    print("para ", n, ":")
    listTime.append(factoresPrimos(n))

print("numeros: ", listNumbers)
print("Tiempos:", listTime)

digitos = [1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.plot(digitos, listTime)
plt.show()