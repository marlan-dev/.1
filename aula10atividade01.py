# Criando uma matriz 3x3
# matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]
# print("Elemento (0,0):", matriz[0][0])  # Saída: 1
# print("Elemento (2,1):", matriz[2][1])  # Saída: 8

# for linha in matriz:
 #   print (f"|", end=" ")
 #   for elemento in linha:
 #       print(elemento, end=' | ')
 #   print()

matriz_4_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    
]


def imprimir_matriz(matriz):
       for linha in matriz:
              print (f"|",end=" ")
              for elemento in linha:
                     print(elemento, end=' | ')
                     print ()



def ler_matriz():
       matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]
       for linha in matriz:
        print(linha)
       
def soma_matrizes():
     soma = 0
     for linha in matriz_4_4:
      soma=soma+sum(linha)
     print(f"Soma dos elementos acima da diagonal principal:  {soma}")
def maior_numero_em_linha():
        for i, linha in enumerate(matriz_4_4):
         print(f"Maior valor da linha {i}: {max(linha)}")
def multiplicacao_matriz():
       num = int(input("Digite o número para multiplicação: "))
       linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))
       matriz_4_4[linha_escolhida] = [num * valor for valor in matriz_4_4[linha_escolhida]]

def pares_e_impares():
i=int
j=int

vet_pares=[]
vet_impares=[]

pares = sum(1 for linha in matriz_4_4 for num in linha if num % 2 == 0)
vet_pares(matriz_4_4[i][j])
print(f"Quantidade de números pares: {pares}")

impares = sum(1 for linha in matriz_4_4 for num in linha if num % 2 == 1)
vet_impares(matriz_4_4[i][j])
print(f"Quantidade de números impares: {impares}")

vet_pares=[]
vet_impares=[]

