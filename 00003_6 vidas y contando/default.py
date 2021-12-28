class Gato:
  def __init__(self,energia, edad):
    self.energia = energia
    self.edad = edad

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
    
    
