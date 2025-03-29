
#matriz = []
#for i in range (4):
  #      linha = []
  #      for j in range(4):
 #           valor = int(input(f"Digite o valor para [{i}][{j}]: "))
 #           linha.append(valor)
 #       matriz.append(linha)

#for linha in matriz:
#        print(linha)


#def imprimir_matriz(matriz):
 #      for linha in matriz:
 #             print (f"|",end=" ")
 #             for elemento in linha:
 #                    print(elemento, end=' | ')
 #                    print ()



matriz_4_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    
]




#oma = 0
#or linha in matriz_4_4:
 #     soma=soma+sum(linha)
#      print(f"Soma dos elementos acima da diagonal principal:  {soma}")

#or i, linha in enumerate(matriz_4_4):
 #  print(f"Maior valor da linha {i}: {max(linha)}")
 #  print(f"\n")

#et_impares=[]
#et_pares = []
#or linha in matriz_4_4:
#   print(linha)

#ares = sum(1 for linha in matriz_4_4 for num in linha if num % 2 == 0)
#et_pares.append(matriz[i][j])
#rint(f"Quantidade de números pares: {pares}")

#mpares = sum(1 for linha in matriz_4_4 for num in linha if num % 2 == 1)
#rnt(f"Quantidade de números impares: {impares}")

num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))
matriz_4_4[linha_escolhida] = [num * valor for valor in matriz_4_4[linha_escolhida]]
for linha in matriz_4_4:
    print(linha)
