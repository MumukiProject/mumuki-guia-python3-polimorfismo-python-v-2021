  
  def test_Le_puedo_especificar_su_plato_del_dia_a_una_instancia_de_chef_inicialmente(self):
    fideos = Pasta()
    mora = Chef(fideos)
    self.assertEqual(mora.plato_del_dia, fideos)
    
  def test_Una_pasta_tiene_inicialmente_0_ajies(self):
    fideos = Pasta()
    self.assertEqual(fideos.ajies, 0)
    
  def test_Una_pizza_inicialmente_tiene_adobo_como_condimento(self):
    muzarella = Pizza()
    self.assertEqual(muzarella.condimento, 'adobo')
    
  def test_Cuando_una_instancia_de_Chef_picantea_una_pasta_que_no_está_muy_picante_la_pasta_pasa_a_tener_5_ajies_más(self):
    fideos = Pasta()
    mora = Chef(fideos)
    mora.picantear()
    self.assertEqual(fideos.ajies, 5)
    
  def test_Cuando_una_instancia_de_Chef_picantea_una_pizza_que_no_está_muy_picante_la_pizza_pasa_a_tener_cayena_de_condimento(self):
    muzarella = Pizza()
    mora = Chef(muzarella)
    mora.picantear()
    self.assertEqual(muzarella.condimento, 'cayena')
    
  def test_Cuando_una_instancia_de_AyudanteDeCocina_suaviza_una_pasta_la_misma_pasa_a_tener_1_aji_menos(self):
    fideos = Pasta()
    fideos.ajies = 5
    roma = AyudanteDeCocina()
    roma.suavizar(fideos)
    self.assertEqual(fideos.ajies, 4)
    
  def test_Cuando_una_instancia_de_AyudanteDeCocina_suaviza_una_pizza_la_misma_pasa_a_tener_oregano_de_condimento(self):
    muzarella = Pizza()
    roma = AyudanteDeCocina()
    roma.suavizar(muzarella)
    self.assertEqual(muzarella.condimento, 'oregano')

    
  def test_Si_una_instancia_de_Chef_quiere_picantear_una_pasta_que_está_demasiado_picante_arroja_una_excepcion(self):
    fideos = Pasta()
    mora = Chef(fideos)
    fideos.ajies = 11
    self.assertRaisesRegex(Exception, "El plato ya está demasiado picante", mora.picantear)
    
  def test_Si_una_instancia_de_Chef_quiere_picantear_una_pizza_que_está_demasiado_picante_arroja_una_excepcion(self):
    muzarella = Pizza()
    mora = Chef(muzarella)
    muzarella.condimento = 'cayena'
    self.assertRaisesRegex(Exception, "El plato ya está demasiado picante", mora.picantear)