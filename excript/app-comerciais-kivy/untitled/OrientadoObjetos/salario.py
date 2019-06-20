class Salario:
    def __init__(self, hora_trabalhada, minuto_trabalhada, valor_salario):
        self.hora_trabalhada = hora_trabalhada
        self.minuto_trabalhada = minuto_trabalhada
        self.valor_salario = valor_salario

    def calcula_salario_bruto(self):
        salario_hora = self.hora_trabalhada * self.valor_salario
        salario_minuto = (self.minuto_trabalhada / 60) * self.valor_salario
        salario_bruto = salario_hora + salario_minuto
        return salario_bruto

    def calcula_imposto_renda(self):
        imposto_renda = (11 * self.calcula_salario_bruto()) / 100
        return imposto_renda

    def calcula_inss(self):
        inss = (8 * self.calcula_salario_bruto()) / 100
        return inss

    def calcula_sindicato(self):
        sindicato = (5 * self.calcula_salario_bruto() / 100)
        return sindicato

    def calcula_salario_liquido(self):
        salario_liquido = self.calcula_salario_bruto() - (self.calcula_imposto_renda() +
                                        self.calcula_inss() + self.calcula_sindicato())
        return salario_liquido


hora = int(input('Informe a Hora Trabalhada: '))
minuto = int(input('Informe os minuto trabalhados: '))
valor_salario = float(input('Informe o valor da hora: '))
salario = Salario(hora, minuto, valor_salario)
print('\nSalario Bruto R$ {:.2f}'.format(salario.calcula_salario_bruto()))
print('Imposto de Renda R$ {:.2f}'.format(salario.calcula_imposto_renda()))
print('INSS R$ {:.2f}'.format(salario.calcula_inss()))
print('Sindicato R$ {:.2f}'.format(salario.calcula_sindicato()))
print('Salario Liquido R$ {:.2f}'.format(salario.calcula_salario_liquido()))
