class Conta:
    def __init__(self, titular, numero, saldo=0.0, limite = 500):
        self.saldo = saldo
        self.titular = titular
        self.numero = numero
        self.limite = limite
 
    def Deposito(self,valor):
        print(f"Saldo inicial: {self.saldo}")
        self.saldo = self.saldo + valor
        print (f"Saldo final : {self.saldo}")

    def saque(self, valor):
        print(f"Saldo inicial: {self.saldo}")
        if (self.saldo - valor) >= -self.limite:
            self.saldo -= valor
            print(f"Valor após o saque {self.saldo}")
        else:
            print("Saldo negado!, voce não tem limite para o saque")

    def info(self):
        print(f"Conta: {self.numero} - {self.titular} - {self.saldo}")

class Banco:
    def __init__ (self):
        self.contas={}
    
if __name__ == "__main__":
    print(f"Criando a primeira conta")
    cc_1=Conta ("00001", "Dom casmurro", 1500.20, 500)
    #cc_1.info()

    #valor_deposito=float(input("Digite o valor para o depósito: "))
    #cc_1.Deposito(valor_deposito)

    valor_saque=float(input("Digite o valor para o saque: "))
    cc_1.saque(valor_saque)
    
    
    
