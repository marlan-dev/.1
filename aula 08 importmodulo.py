import sys 

def principal(parametros):
    for dado in parametros:
        print(dado)

def soma (numeros) :
    somatorio=0
    for valor in numeros:
        somatorio = somatorio + float(valor)
        #print(f"O valor da soma dos números é {somatorio}")
        return somatorio
    
    #

def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def testar_fatorial ():
    numero=int(input("\n\n\tInforme um numero: "))
    resultado=fatorial(numero)
    print(f"\n\n\tfatorial de {numero} é igual à {resultado}\n\n")

if __name__ == "__main__":


  # resultado=soma(sys.argv[1:])
  # print (f"O valor da soma dos numeros é {resultado}")

    testar_fatorial()
