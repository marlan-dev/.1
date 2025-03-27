numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
numero3=int(input("Digite o terceiro número: "))
numero4=int(input("Digite o quarto número: "))
numero5=int(input("Digite o quinto número: "))

lista = [numero1, numero2, numero3, numero4, numero5]

def soma_dos_numeros(lista):
    soma= sum(lista)
    print(f"A soma dos numeros são: {soma}")
    

#
    

def numeros_ordenados():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    num3=int(input("Digite o terceiro número: "))
    num4=int(input("Digite o quarto número: "))
    num5=int(input("Digite o quinto número: "))
    lista=[num1, num2, num3, num4, num5]
    lista_ordenada=sorted(lista)
    print(f"Os números em ordem são: {lista_ordenada}")

def impares_no_intervalo ():
    lista=[]
    for i in range (1,51,2):
        lista.append(i)
    print (f"Os elements da lista são {lista}")



def pares_no_intervalo():
    lista=[]
    for i in range(0,51,2):
        lista.append(i)
    print(f"Os números pares são: {lista}")

if __name__ == "__main__":
    #numeros_ordenados()
    #impares_no_intervalo ()
    #pares_no_intervalo()
    soma_dos_numeros(lista)