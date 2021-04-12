import time

def factoresPrimos(num):

    primos = []
    inicio = time.time()
    print(inicio)
    for i in range(2,num + 1):

        while num % i == 0:
            primos.append(i)
            num = num / i
    fin = time.time()
    print(fin)
    tiempo = float(fin - inicio)
    print("El tiempo de procesamiento fue:", tiempo)
    return primos


print(factoresPrimos(425869237))

