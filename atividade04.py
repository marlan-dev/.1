idade=int(input("Digite sua idade: "))
acompanhada=(input("Está acompanhada?"))
banido=(input("Está banido?"))

if (idade >=18) or (acompanhada == "Sim") and (banido == "nao"):
    print("entrada permitida.")
else:
    print("entrada negada")

