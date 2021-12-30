  
  def test_El_método_rehabilitar_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    agus = EstudianteDeVeterinaria()
    self.assertTrue("rehabilitar" in dir(agus) and callable(agus.rehabilitar))
    
  #VER COMO TESTEAR LA EXCEPCIÓN