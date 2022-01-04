 
 def test_Una_planta_carnivora_zombi_es_un_peligro_si_tiene_mas_de_40_de_clorofila(self):
    mora = PlantaCarnivoraZombi(41)
    self.assertTrue(mora.es_un_peligro())