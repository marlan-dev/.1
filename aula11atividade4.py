aluno1 = {"nome" : "Marcos", "notas" : [4, 8, 8]}
aluno2 = {"nome" : "João", "notas" : [6, 10, 10]}
aluno3 = {"nome" : "Paulo", "notas" : [8, 5, 10]}


print (f"dados do aluno 1 {aluno1}")
print (f'As notas do aluno {aluno1["nome"]} são {aluno1["notas"]}')

media = sum (aluno1["notas"]) / len (aluno1["notas"])
print (f'O aluno {aluno1["nome"]} obteve media igual a: {media}')

aluno1["media"]= media
print(f" Dados do aluno 1 {aluno1}")