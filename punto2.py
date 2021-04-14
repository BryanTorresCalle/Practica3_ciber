import time
from hashlib import sha256
import random as rand
import matplotlib.pyplot as plt


def punto2():
    n = int(input("Ingrese un número entre 1 y 9 "))
    interacciones = 0
    while n < 1 or n > 10:
        n = int(input("Ingrese un número entre 1 y 9 "))
        print ("Ingrese un n valido")

    while True:
        inicio = time.time()
        x = str(rand.randint(1,100000))
        hash_val = sha256(x.encode()).hexdigest()
        interacciones += 1
        if hash_val[0:n] == n*'0':
            fin = time.time()
            tiempo = float(fin - inicio)
            return [interacciones, tiempo,n]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listTime = []
    listIterations = []
    listN = []
    n = [1,2,3,4,5]
    for n in range (5):
        returns = punto2()
        listTime.append(returns[1])
        listIterations.append(returns[0])
        listN.append(returns[2])
    plt.plot(listN, listIterations)
    plt.ylabel('Cantidad de iteraciones')
    plt.xlabel('n seleccionado')
    plt.show()
    print(listN)
    print(listIterations)
