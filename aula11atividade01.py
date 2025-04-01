pessoa = {"nome" : "Papagaio", "idade": 49, "cidade" : "petropolis"}
print(f"Dados da pessoa: {pessoa}")

pessoa["idade"]=48
print(f"Dados atualizado: {pessoa}")

pessoa["email"]="luis.rodrigo.net@gmail.com"
print(f"Dados Atualizados: {pessoa}")

pessoa["sexo"]="Masculino"
print(f"Dados atualizados: {pessoa}")

del pessoa["nome"]
del pessoa["email"]
print(f"Dados atualizado {pessoa}")

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Método 1: update()
d1.update(d2)

# Método 2: operador ** (Python 3.9+)
d3 = {**d1, **d2}

print("Resultado:", d1)