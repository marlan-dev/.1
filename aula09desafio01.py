numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
numero3=int(input("Digite o terceiro número: "))
numero4=int(input("Digite o quarto número: "))
numero5=int(input("Digite o quinto número: "))

lista = [numero1, numero2, numero3, numero4, numero5]

def soma_dos_numeros(lista):
    soma= sum(lista)
    print(f"A soma dos numeros são: {soma}")
    soma_dos_numeros(lista)
    lista_ordenada=sorted(lista)
    print(f"Os números em ordem são: ")

if __name__ == "__main__":
    soma_dos_numeros(lista)
    lista_ordenada=sorted(lista)
    print(f"Os números em ordem são: ")

