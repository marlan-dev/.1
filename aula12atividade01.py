class Veiculo:
    def __init__(self, marca, modelo,ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, placa, cor):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas
        self.placa = placa

    def exibir_info(self):
        super().exibir_info()
        print(f"Este carro tem {self.portas} portas.")
        print(f"A placa desse carro é {self.placa}")
        print(f"A cor desse carro é {self.cor}")

if __name__ == "__main__" :
    meu_carro = Carro("Toyota", "Corolla", 2020, 4, "9kk-igt", "Vermelho")
    meu_carro.exibir_info()

class Animal:
    def fazer_som(self):
        pass 

    class Cachorro(Animal):
        def fazer_som(self):
            print("Au Au!")

    class gato (Animal):
        def fazer_som(self):
            print("Miau!")

    def fazer_barulho(Animal):
        Animal.fazer_som()