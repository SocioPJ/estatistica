import numpy as np

x = input("Digite xi: (separado por espaços) - ").split(" ")
x = np.array(list(map(int, x)))
P = input("Digite P: (separado por espaços) - ").split(" ")
P = np.array(list(map(float, P)))

try:
    media = np.sum(x * P)
    variancia = np.sum(P * x**2) - media ** 2
    dp = np.sqrt(variancia)
    
    print("Média: %.2f" % media)
    print("Variância: %.2f" % variancia)
    print("Desvio padrão: %.2f" % dp)
except:
    if len(x) != len(P):
        print("Erro: x e P devem ter o mesmo tamanho")
        exit()
    elif sum(P) != 1:
        print("Erro: P devem somar 1")
        exit()