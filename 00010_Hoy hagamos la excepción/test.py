  
  def test_Si_no_se_puede_atacar_a_un_zombi_porque_es_peligroso_se_lanza_la_excepcion_correspondiente(self):
    hecate = Sobreviviente(100)
    caliope = Zombi(100)
    self.assertRaisesRegex(AssertionError, "'Sobreviviente' Es peligroso atacar a este zombi", hecate.atacar, caliope)
    
  #self.assertRaisesRegex(AttributeError, "'Gato' object has no attribute 'recibir_rehabilitacion'$", agus.rehabilitar, morfeo)