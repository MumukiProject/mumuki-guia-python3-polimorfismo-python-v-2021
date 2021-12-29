class Caballo:
  def __init__(self,energia, raza):
    self.energia = energia
    self.raza = raza

  def comer(self,gramos):
    self.energia += gramos * 2

  def galopar(self,kms):
    self.energia -= kms

class Golondrina:
  def __init__(self,energia, ciudad):
    self.energia = energia
    self.ciudad = ciudad

  def comer(self,gramos):
    self.energia += gramos / 2

  def volar_hacia(self,destino):
    self.ciudad = destino
    self.energia /=  2 
    
