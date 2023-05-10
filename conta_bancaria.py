class Conta:
  def __init__(self, numero_conta, titular, saldo):
    self.numero_conta = numero_conta
    self.titular = titular
    self.saldo = saldo
  def depositar(self, numero_conta, novo_valor):
    if novo_valor > 0:
      self.saldo += novo_valor
    else:
      raise Exception("Valor inválido")
  def sacar():
    