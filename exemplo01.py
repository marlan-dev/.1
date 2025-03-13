idade=int(input("Informe sua idade:  "))
habilitado=input("possui carteira de habilitação <s/n> : ")
habilitado=habilitado.lower

if (idade >= 18) and (habilitado =="s"):
    print("Você pode dirigir")
else:
    print("Voce não pode dirigir")
