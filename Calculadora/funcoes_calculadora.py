"""
Funções que executarão o cálculo dos
"""
def somar(numero1, numero2):
    return print("Resultado: ",numero1 + numero2)

def multiplicar (numero1, numero2):
    return print("Resultado: ",numero1 * numero2)

def dividir (numero1, numero2):
    try:
        divisao = numero1/numero2
    except ZeroDivisionError:
        return print("Não é possível dividir {} por 0".format(numero1))
    return print("Resultado: ", divisao)

def subtrair(numero1, numero2):
    return print("Resultado: ",numero1 - numero2)

