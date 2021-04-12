from hashlib import sha256
import random as rand

def punto2():
    n = int(input("Ingrese un número entre 1 y 9 "))
    interacciones = 0
    while n < 1 or n > 10:
        n = int(input("Ingrese un número entre 1 y 9 "))
        print ("Ingrese un n valido")

    while True:
        x = str(rand.randint(1,100000))
        hash_val = sha256(x.encode()).hexdigest()
        interacciones += 1
        if hash_val[0:n] == n*'0':
            return "El hash es", hash_val, " con ", interacciones, " interacciones"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(punto2())

