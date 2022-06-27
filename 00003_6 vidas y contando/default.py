class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
    
    
