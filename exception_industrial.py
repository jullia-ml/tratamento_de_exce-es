class ValorInvalidoError(Exception):
    pass

class SistemaIndustrial:
    def __init__(self, sensor_temperatura):
        self.sensor_temperatura = sensor_temperatura

    def iniciar_leitura(self):
        if type(self.sensor_temperatura) == str or type(self.sensor_temperatura) == float:
            raise ValorInvalidoError(
               "Apenas numeros inteiros são válidos!")

        elif self.sensor_temperatura >= 90:
            print("Superaquecendo!")

dados = SistemaIndustrial(90)

try:
   dados.iniciar_leitura()
except ValorInvalidoError as e:
   print(f"{e}")
finally:
 print("Memória fechando...")
