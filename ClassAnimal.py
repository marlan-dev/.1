class Animal:
    def fazer_som(self):
        pass 

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

def fazer_barulho(Animal):
    Animal.fazer_som()

meu_cachorro = Cachorro()
meu_gato = Gato()

fazer_barulho(meu_cachorro)
fazer_barulho(meu_gato)
