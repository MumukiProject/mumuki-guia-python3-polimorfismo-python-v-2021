
  def test_El_método_alimentar_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    agus = EstudianteVeterinaria()
    self.assertTrue("alimentar" in dir(agus) and callable(agus.alimentar))
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_alimentar_a_una_instancia_de_Gato_con_300_gramos(self):
    agus = EstudianteVeterinaria()
    kali = Gato(100, 13)
    agus.alimentar(kali,300)
    self.assertEqual(kali.energia, 400)
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_alimentar_a_una_instancia_de_Caballo_con_800_gramos(self):
    agus = EstudianteVeterinaria()
    nano = Caballo(100, 'Cuarto de Milla')
    agus.alimentar(nano,800)
    self.assertEqual(nano.energia, 1700)
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_alimentar_a_una_instancia_de_Golondrina_con_40_gramos(self):
    agus = EstudianteVeterinaria()
    pepita = Golondrina(100, 'General las Heras')
    agus.alimentar(pepita, 40)
    self.assertEqual(pepita.energia, 120)