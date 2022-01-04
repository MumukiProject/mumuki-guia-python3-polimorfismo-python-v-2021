  
  def test_Si_no_se_puede_atacar_a_un_zombi_porque_es_peligroso_se_lanza_la_excepcion_correspondiente(self):
    hecate = Sobreviviente(100)
    caliope = Zombi(100)
    self.assertRaisesRegex(Exception, "Es peligroso atacar a este zombi", hecate.atacar, caliope)
    
  def test_Una_planta_carnivora_zombi_es_un_peligro_si_tiene_mas_de_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(41)
    self.assertTrue(mora.es_un_peligro())
    