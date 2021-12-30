Definir comportamiento en esas 3 clases donde una interactúa con las otras dos polimórficamente. Introducir la idea de excepciones y que lancen una (ver si esto va en un ejercicio aparte entre el 8 y el 9).

class Sobreviviente:
  def __init__(self, una_adrenalina):
    self.adrenalina = una_adrenalina

  def atacar(self, un_zombi):
    if not un_zombi.es_un_peligro():
      un_zombi.recibir_danio(self.adrenalina / 2)
      self.adrenalina += 20
    else:
      raise Exception('Es peligroso atacar a este zombi')

class SuperZombi:
  def __init__(self, una_salud):
    self.salud = una_salud

  def sabe_correr(self):
    return True

  def recibir_danio(self, puntos_danio):
    self.salud = max(self.salud - puntos_danio, 0)

  def es_un_peligro(self):
    return True
  
  def regenerarse(self):
    self.salud = 100

class Zombi:
  def __init__(self, una_salud):
    self.salud = una_salud
 
  def sabe_correr(self):
    return True

  def recibir_danio(self, puntos_danio):
    self.salud =  max(self.salud - (puntos_danio * 2), 0)

  def es_un_peligro(self):
    self.salud > 50