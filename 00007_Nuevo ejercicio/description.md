Hacerle una pregunta al objeto que se comunica con los otros que dependa de su objeto atributo. El objetivo es tratar encapsulamiento, responsabilidad y polimorfismo, tendría que ser una solución que se preste a resolverlo con if pero para ver que hay una opción superadora

class EstudianteDeVeterinaria:

  def alimentar_animal(self,animal, gramos):
    animal.comer(gramos)

  def rehabilitar(self,animal):
    animal.recibir_rehabilitacion()

  def puede_dar_el_alta(self,animal):
    return animal.esta_feliz()

class Gato:
  def __init__(self, energia, edad):
    self.energia = energia
    self.edad = edad

  def comer(self, gramos):
    self.energia += gramos / 2

  def cumplir_anios(self):
    self.edad += 1
  
  def recibir_rehabilitacion(self):
    self.comer(400)

  def esta_feliz(self):
    return self.energia > 30

class Caballo:
  def __init__(self, energia, raza):
    self.energia = energia
    self.raza = raza

  def comer(self, gramos):
    self.energia += gramos * 2

  def galopar(self, kms):
    self.energia -= kms

  def recibir_rehabilitacion(self):
    self.galopar(3)
    self.comer(3000)
    self.galopar(5)

  def esta_feliz(self):
    return True

class Golondrina:
  def __init__(self, energia, ciudad):
    self.energia = energia
    self.ciudad = ciudad

  def comer(self, gramos):
    self.energia += gramos

  def volar_hacia(self, una_ciudad):
    self.ciudad = una_ciudad
    self.energia /= 2
  
  def recibir_rehabilitacion(self):
    self.volar_hacia("Lihuel Calel")
  
  def esta_feliz(self):
    return self.ciudad = "Lihuel Calel"