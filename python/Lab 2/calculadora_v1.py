print("\n***** Calculadora em Python *****")

op = input("\nEscolha a operação (+, -, *, /): ")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

if op == '+':
    print(f"\nResultado: {n1} + {n2} = {n1 + n2}")
elif op == '-':
    print(f"\nResultado: {n1} - {n2} = {n1 - n2}")
elif op == '*':
    print(f"\nResultado: {n1} * {n2} = {n1 * n2}")
elif op == '/':
    print(f"\nResultado: {n1} / {n2} = {n1 / n2}" if n2 != 0 else "\nErro! Divisão por zero.")
else:
    print("\nOperação inválida.")

