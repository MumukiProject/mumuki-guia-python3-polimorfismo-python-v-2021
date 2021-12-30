  
  def test_El_método_rehabilitar_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    agus = EstudianteDeVeterinaria()
    self.assertTrue("rehabilitar" in dir(agus) and callable(agus.rehabilitar))
    
  def test_El_método_rehabilitar_hace_que_un_animal_reciba_rehabilitacion(self): 
    morfeo = Gato(100, 1000)
    agus = EstudianteDeVeterinaria()
    self.assertRaisesRegex(AttributeError, "'Gato' object has no attribute 'recibir_rehabilitacion'$", agus.rehabilitar, morfeo)