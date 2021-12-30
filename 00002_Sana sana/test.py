  
  def test_El_método_rehabilitar_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    agus = EstudianteDeVeterinaria()
    self.assertTrue("rehabilitar" in dir(agus) and callable(agus.rehabilitar))
    
  def test_El_método_rehabilitar_hace_que_un_animal_reciba_rehabilitacion(self): 
    morfeo = Golondrina(100, "Las Heras")
    agus = EstudianteDeVeterinaria()
    #self.assertRaises(AttributeError, agus.rehabilitar, morfeo)
    self.assertRaisesRegex(AttributeError, "'Gato' object has no attribute 'recibir_rehabilitacion'$", agus.rehabilitar, morfeo)