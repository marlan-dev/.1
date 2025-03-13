SENHA_CORRETA="1234a"

idade=int(input("informe a sua idade: "))

if (idade>=18):
    senha=input("informe a senha de acesso :")
    if(senha==SENHA_CORRETA):
        print(" ACESSO LIERADO")
    else:
        print("ACESSO NEGADO - SENHA")
else:
    print ("ACESSO NEGADO - IDADE")
