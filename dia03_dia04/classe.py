from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        """defina na classe filha"""

    @abstractmethod
    def andar(self):
        """defina a classe filha"""

class Cachorro(IAnimal):
    def falar(self):
        print("AuAu")

    def andar(self):
        print("ando com 4 patas")

class Pessoa:

    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self.idade = idade
        self.__humano = True

    def fala_pessoa(self):
        print("Falando")

    def mostra_nome(self):
        print("nome")    

pingo = Cachorro()
pingo.falar()
pingo.andar()

humano = Pessoa("André, 21")

humano.fala_pessoa()
humano.mostra_nome


