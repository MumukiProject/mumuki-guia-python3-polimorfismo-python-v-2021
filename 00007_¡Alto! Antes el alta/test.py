  
  def test_El_método_puede_dar_el_alta_está_definido_en_la_clase_EstudianteDeVeterinaria(self):
    theo = Gato(0,7)
    self.assertTrue("recibir_rehabilitacion" in dir(theo) and callable(theo.recibir_rehabilitacion))
    
  def test_Un_gato_está_feliz_si_tiene_más_de_30_de_energia(self):
    kali = Gato(31, 13)
    self.assertTrue(kali.esta_feliz())
    
  def test_Un_gato_no_está_feliz_si_tiene_30_de_energia(self):
    kali = Gato(30, 13)
    self.assertFalse(kali.esta_feliz())
    
  def test_Un_caballo_está__siempre_feliz(self):
    nano = Caballo(0, 'Cuarto de milla')
    self.assertTrue(nano.esta_feliz())
    
  def test_Una_golondrina_está_feliz_cuando_su_ciudad_es_Lihuel Calel(self):
    norita = Golondrina(0, 'Lihuel Calel')
    self.assertTrue(norita.esta_feliz())
    
  def test_Una_golondrina_no_está_feliz_cuando_su_ciudad_no_es_'Lihuel Calel'(self):
    norita = Golondrina(0, 'Quilmes')
    self.assertFalse(norita.esta_feliz())
    
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_dar_el_alta_a_un_gato_si_está_feliz(self):
    ramona = EstudianteDeVeterinaria()
    theo = Gato(31,7)
    self.assertTrue(ramona.puede_dar_el_alta(theo))
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_no_puede_dar_el_alta_a_un_gato_si_no_está_feliz(self):
    ramona = EstudianteDeVeterinaria()
    theo = Gato(30,7)
    self.assertFalse(ramona.puede_dar_el_alta(theo))
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_dar_el_alta_a_una_golondrina_si_está_feliz(self):
    ramona = EstudianteDeVeterinaria()
    norita = Golondrina(0, 'Lihuel Calel')
    self.assertTrue(ramona.puede_dar_el_alta(norita))
    
  def test_Una_instancia_de_EstudianteDeVeterinaria_no_puede_dar_el_alta_a_una_golondrina_si_no_está_feliz(self):
    ramona = EstudianteDeVeterinaria()
    norita = Golondrina(0, 'Quilmes')
    self.assertFalse(ramona.puede_dar_el_alta(norita))
  
  def test_Una_instancia_de_EstudianteDeVeterinaria_puede_darle_el_alta_a_un_caballo(self):
    ramona = EstudianteDeVeterinaria()
    nano = Caballo(0, 'Cuarto de Milla')
    self.assertTrue(ramona.puede_dar_el_alta(nano))  