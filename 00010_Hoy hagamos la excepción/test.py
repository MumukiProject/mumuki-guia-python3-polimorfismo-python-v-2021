  
  def test_Si_no_se_puede_atacar_a_un_zombi_porque_es_peligroso_se_lanza_la_excepcion_correspondiente(self):
    hecate = Sobreviviente(100)
    caliope = Zombi(100)
    self.assertRaisesRegex(Exception, "Es peligroso atacar a este zombi", hecate.atacar, caliope)
    
  def test_Si_un_sobreviviente_con_40_de_adrenalina_ataca_a_un_zombi_no_peligroso_lo_hace_con_20_de_daño(self):
    morfeo = Sobreviviente(40)
    burgess = Zombi(48)
    morfeo.atacar(burgess)
    self.assertEqual(burgess.hambre,  8)
    
