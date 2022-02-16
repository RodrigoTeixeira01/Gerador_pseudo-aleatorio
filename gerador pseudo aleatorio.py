from math import *
def rand(seed):
    a = seed
    return int(((a**2*2*3.1416-a**2)/8+a**2)*100)
seed=int(input("Digite a seed: "))
aleatorios=""
continuar=True
while continuar:
    try:
        seed=rand(seed)
        aleatorios=f"{aleatorios}{seed}"
    except:
        continuar=False
input(aleatorios)
