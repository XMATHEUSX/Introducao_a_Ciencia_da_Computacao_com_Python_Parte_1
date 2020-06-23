import math 

def delta(a, b, c):
    return b**2 - 4*a*c



def imprime_raizes(a,b,c):
    valor_delta = delta(a,b,c)
    if valor_delta == 0:
        x_1 = (-b + math.sqrt(valor_delta)) / (2*a)
        print("Raiz única:", x_1)
    else:
        if valor_delta < 0 :
            print("Esta equação não possui raizes reais")
        else:
            x_1 = (-b + math.sqrt(valor_delta)) / (2*a)
            x_2 = (-b - math.sqrt(valor_delta)) / (2*a)
            print("A Primeira Raiz é :", x_1)
            print("A Segunda Raiz: é ", x_2)

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a,b,c)

main()