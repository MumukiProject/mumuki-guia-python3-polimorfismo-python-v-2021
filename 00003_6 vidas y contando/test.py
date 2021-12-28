  
  def test_El_método_recibir_rehabilitacion_está_definido_en_la_clase_Gato(self):
    theo = Gato(0,7)
    self.assertTrue("recibir_rehabilitacion" in dir(theo) and callable(theo.recibir_rehabilitacion))
    
  def test_Cuando_un_gato_recibe_rehabilitación_come_400_gramos_de_comida(self):
    kali = Gato(0, 13)
    kali.recibir_rehabilitacion()
    self.assertEqual(kali.energia, 400)