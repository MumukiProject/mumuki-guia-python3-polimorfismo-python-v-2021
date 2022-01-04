  def test_Si_creo_un_nuevo_Sobreviviente_le_puedo_especificar_su_adrenalina_inicial(self):
    sobreviviente = Sobreviviente(10)
    self.assertEqual(sobreviviente.adrenalina,10)
    
   def test_El_método_atacar_está_definido_en_la_clase_Sobreviviente(self):
    morfeo = Sobreviviente(100)
    self.assertTrue("atacar" in dir(morfeo) and callable(morfeo.atacar))
    
   def test_Si_un_sobreviviente_ataca_a_un_zombi_que_no_es_peligroso_su_adrenalina_aumenta_en_20(self):
    morfeo = Sobreviviente(100)
    burgess = Zombi(0)
    self.assertEqual(morfeo.adrenalina, 120)
    
   def test_Si_un_sobreviviente_con_30_de_adrenalina_ataca_a_un_zombi_con_hambre_inicial_40_su_hambre_queda_en_25(self):
    morfeo = Sobreviviente(30)
    burgess = Zombi(40)
    self.assertEqual(burgess.hambre, 25)
    
   def test_Si_un_sobreviviente_con_100_de_adrenalina_ataca_a_un_zombi_con_hambre_inicial_30_su_hambre_queda_en_0(self):
    morfeo = Sobreviviente(100)
    burgess = Zombi(30)
    self.assertEqual(burgess.hambre, 0)
    
  # Que tire excepción cuando es un SuperZombi y cuando el hambre de un zombi es > 500
  