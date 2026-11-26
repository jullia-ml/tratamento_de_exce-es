class TentativasIncorretas(Exception):
    pass

class CofreDigital:
    def __init__(self):
        self.tentativas_permitidas = 2
        self.qtd_tentativas = 0
        self.senha = "senha123online"

    def acesso_ao_cofre(self):
        inserir_senha = input("Digite a senha: ")
        while inserir_senha != self.senha:
            self.qtd_tentativas += 1
            print("A senha inserida não corresponde com a atual, tente novamente:")
            inserir_senha = input()
            if self.qtd_tentativas >= self.tentativas_permitidas:
                raise TentativasIncorretas(
                    "Você teve apenas 3 tentativas. Acesso bloqueado"
                )
        else:
            print("Acesso permitido")

attempts = CofreDigital()
try:
    attempts.acesso_ao_cofre()
except TentativasIncorretas as e:
    print(f"Erro: {e}")
