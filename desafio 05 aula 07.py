def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n +1):
            resultado *= i
        return resultado
    
numero = int(input("Digite um número inteiro não negativo: "))
if numero < 0:
    print("Por favor, Digite um número nao negativo")
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}.")