from Calculadora.funcoes_calculadora import *

print("***Calculadora***")

continuar = "S"

while continuar =="S":
    try:
        num1 = int(input("Informe o 1° número: "))
        num2 = int(input("Informe o 2° número: "))
    except ValueError:
        print("Por favor, digite um valor válido")
        continue

    operador = input("Qual operação você deseja realizar\n? (+) (-) (*) (+)")

    if operador =="+":
        print("")
        total_soma = somar(num1,num2)

    elif operador =="-":
        print("")
        total_subtracao = subtrair(num1,num2)

    elif operador == "*":
        print("")
        total_mulplicacao = multiplicar(num1,num2)

    elif operador == "/":
        print("")
        total_divisao = dividir(num1,num2)

    else:
        print("Operador inválido")

    continuar=input("Deseja realizar outra operação\n? Digite SIM para continuar").upper()
