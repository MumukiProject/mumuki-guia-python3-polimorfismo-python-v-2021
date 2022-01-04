  
  def test_Si_no_se_puede_atacar_a_un_zombi_porque_es_peligroso_se_lanza_la_excepcion_correspondiente(self):
    hecate = Sobreviviente(100)
    caliope = Zombi(100)
    self.assertRaisesRegex(Exception, "Es peligroso atacar a este zombi", hecate.atacar, caliope)
    
  def test_Una_planta_carnivora_zombi_es_un_peligro_si_tiene_mas_de_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(41)
    self.assertTrue(mora.es_un_peligro())
    
  def test_Una_planta_carnivora_zombi_al_recibir_danio_pierde_10_de_clorofila(self):
    mora = PlantaCarnivoraZombi(30)
    mora.recibir_danio(20)
    self.assertEqual(mora.clorofila, 20)
    
  def test_Si_una_planta_carnivora_zombi_hace_fotosintesis_por_30_minutos_su_clorofila_aumenta_en_30(self):
    mora = PlantaCarnivoraZombi(30)
    mora.fotosintesis(30)
    self.assertEqual(mora.clorofila, 60)
  
  