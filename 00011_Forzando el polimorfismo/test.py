
  def test_Una_planta_carnivora_zombi_es_un_peligro_si_tiene_mas_de_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(41)
    self.assertTrue(mora.es_un_peligro())
    
  def test_Una_planta_carnivora_zombi_no_es_un_peligro_si_tiene_menos_de_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(39)
    self.assertFalse(mora.es_un_peligro())
    
  def test_Una_planta_carnivora_zombi_no_es_un_peligro_si_tiene_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(40)
    self.assertFalse(mora.es_un_peligro())
    
  def test_Una_planta_carnivora_zombi_al_recibir_danio_pierde_10_de_clorofila(self):
    mora = PlantaCarnivoraZombi(30)
    mora.recibir_danio(20)
    self.assertEqual(mora.clorofila, 20)
    
  def test_Si_una_planta_carnivora_zombi_hace_fotosintesis_por_30_minutos_su_clorofila_aumenta_en_30(self):
    mora = PlantaCarnivoraZombi(30)
    mora.hacer_fotosintesis(30)
    self.assertEqual(mora.clorofila, 60)