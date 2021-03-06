class CalculadorSolar:
    def __init__(self, irradiance, potencia, perda=0.2):

        if not irradiance > 0:
            return 'Falta o valor de irradiação solar'

        if not potencia > 0:
            return 'Falta o valor de potencia da placa solar'

        self.irradience = float(irradiance)
        self.potencia = float(potencia) / 1000
        self.perda = float(perda)

    def diario(self):
        return round(self.irradience * self.potencia *
                     (1 - self.perda), 2)

    def diarioUnit(self):
        diario = str(self.diario()).replace('.', ',')
        return f'{diario} KWh/dia'

    def mensal(self):
        return self.diario() * 30

    def mensalUnit(self):
        mensal = str(self.mensal()).replace('.', ',')
        return f'{mensal} KWh/mês'


if __name__ == "__main__":
    # execute only if run as a script
    irradiance = 4.5  # kWh/m²
    potencia = 410  # W
    perda = 0.2  # 20%/100%

    energia = CalculadorSolar(irradiance, potencia, perda)
    print(energia.diario())
    print(energia.diarioUnit())
    print(energia.mensal())
    print(energia.mensalUnit())
