def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for a in range(1, n + 1):
            resultado *= a
        return resultado
# Exemplo de chamada
print("Fatorial de 5:", fatorial(5))