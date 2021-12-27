class EstudianteDeVeterinaria:
  def __init__(self, animal):
    self.animal

  def alimentar_animal(self, gramos):
    self.animal.comer(gramos)

  def rehabilitar(self):
    self.animal.recibir_rehabilitacion()

class Gato:
  def __init__(self, energia, edad):
    self.energia = energia
    self.edad = edad

  def comer(self, gramos):
    self.energia += gramos / 2

  def cumplir_anios(self):
    self.edad += 1

  def quiere_comer(self):
    return energia < 30
  
  def recibir_rehabilitacion(self):
    self.comer(400)
    
class Golondrina:
  def __init__(self,energia, ciudad):
    self.energia = energia
    self.ciudad = ciudad
    
  def comer(self,gramos):
    self.energia += gramos / 2
    
  def volar_hacia(self,destino):
    self.ciudad = destino
    self.energia /=  2
    
class Caballo:
  def __init__(self,energia, raza):
    self.energia = energia
    self.raza = raza
    
  def comer(self,gramos):
    self.energia += gramos * 2
    
  def galopar(self,kms):
    self.energia -= kms

pelu = EstudianteDeVeterinaria()
theo = Gato(30, 7)
tornado = Caballo(250, "Mustang")
norita = Golondrina(20, "Epecuén")