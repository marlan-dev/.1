"""
Aula 09 - Atividade 01
"""
vet_dados=[5, 8, 15, 25, 40]
vetor1=[5, 10, 15, 20, 25]
vetor_2=[5, 5, 5, 10, 12]
vetor3=[3, 3, 3, 5, 8]

def criar_imprimir_lista ():
    vetor=[5, 8, 15, 25, 40]
    print(f"\n\tO conteúdo do vetor é {vetor}\n")

def criar_imprimir_lista_v2 (vetor):
    print (f"\n\tO conteúdo do vetor é {vetor}\n")


def interando_lista(vetor):
    for elemento in vetor:
        print("\n\tElemento: ", elemento)

# -----------------------------------------------------

def somar_vetores(vetor):
    soma=sum(vetor)
    print("Soma dos elementos: ", soma)

# -----------------------------------------------------



def maior_ou_menor_valor(vetor):
    maior = max(vetor)
    menor = min(vetor)
    print("Maior valor: ", maior)
    print("Menor valor: ", menor)


# -----------------------------------------------------




def inverter_os_elementos(vetor):
    vetor_invertido = vetor[::-1]
    print("\nVetor invertido: ", vetor_invertido)

# -----------------------------------------------------

 

def mult_por_2(vetor):
    multiplicador = 2
    vetor_mult = [elemento * multiplicador for elemento in vetor]
    print("\nVetor multiplicado\n", vetor_mult)

# -----------------------------------------------------

 

def contar_quantidade_de_elementos(vetor):
    ocorrencias = vetor.count(3)
    print("\n\tO total de 3 contados são: ", ocorrencias)

# -----------------------------------------------------

 

def ordenar_vetor_crescente(vetor):
    vetor_ordenado= sorted(vetor)
    print("Vetor ordenado: ", vetor_ordenado)


# -----------------------------------------------------

 

def remover_elementos_duplicados(vetor):
    vetor_nao_duplicados= list(dict.fromkeys(vetor))
    print("Vetor sem duplicatas: ", vetor_nao_duplicados)

# -----------------------------------------------------

 

def separar_elementos_impares_de_pares(vetor):
    pares = [num for num in vetor if num % 2 == 0]
    impares= [num for num in vetor if num % 2 != 0]
    print("Pares: ", pares)
    print("Impares: ", impares)

# -----------------------------------------------------

 

def calcular_media_e_exibir_elementos_acima(vetor):
    media=sum(vetor) / len(vetor)
    acima_media = [num for num in vetor if num > media]
    print("Média: ", media)
    print("Elementos acima da média: ", acima_media)



if __name__ == "__main__":

    #criar_imprimir_lista(vetor1)
    #criar_imprimir_lista_v2(vetor1)
    #interando_lista(vetor1)
    #calcular_media_e_exibir_elementos_acima(vetor1)
    #separar_elementos_impares_de_pares(vetor1)
    #remover_elementos_duplicados(vetor_2)
    #ordenar_vetor_crescente(vetor_2)
    #contar_quantidade_de_elementos(vetor3)
    #mult_por_2(vetor1)
    #inverter_os_elementos(vetor1)
    #maior_ou_menor_valor(vetor3)
    somar_vetores(vetor_2)


    
