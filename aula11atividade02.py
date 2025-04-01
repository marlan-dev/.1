d3=d1= {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print (f"dicionario originais:")
print (f"D1                   : {d1}")
print (f"D2                   :  {d2}")

# Método 1: update()
d1.update(d2)
d2.update(d3)
# Método 2: operador ** (Python 3.9+)
d3 = {**d1, **d2}

print(f"Dicionarios atualizados:")
print(f"D1                 :{d1}")
print(f"D2                 :{d2}")