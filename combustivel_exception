class QuantidadeInvalidaError(Exception):
    pass

class Bomba_de_Combustivel:
    def __init__(self):
        self.tanque_principal_limite = 500

    def abastecer(self, litros):
        if litros > self.tanque_principal_limite:
            raise QuantidadeInvalidaError("Os litros solicitados estão acima do nosso limite!")

        else:
            total = self.tanque_principal_limite - litros
            print(f"A veículo está recebendo {litros} litros de combustivel. E a quantidade de litros atual do tanque é {total}")


cliente = Bomba_de_Combustivel()
try:
    cliente.abastecer(89)
except QuantidadeInvalidaError as e:
    print(f"Erro: {e}")
