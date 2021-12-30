  
  def test_El_método_rehabilitar_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    agus = EstudianteDeVeterinaria()
    self.assertTrue("rehabilitar" in dir(agus) and callable(agus.rehabilitar))
    
  def test_El_método_rehabilitar_hace_que_un_animal_reciba_rehabilitacion(self): 
    morfeo = gato(100, 1000)
    agus = EstudianteDeVeterinaria()
    agus.rehabilitar(morfeo)
    self.assertEqual(morfeo.energia, 1000)
  #VER COMO TESTEAR LA EXCEPCIÓN