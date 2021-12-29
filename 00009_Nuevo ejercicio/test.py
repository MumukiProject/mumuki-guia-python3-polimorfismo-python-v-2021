  
   def test_El_método_atacar_está_definido_en_la_clase_Sobreviviente(self):
    morfeo = Sobreviviente(100)
    self.assertTrue("atacar" in dir(morfeo) and callable(morfeo.atacar))
    
   def test_Si_un_sobreviviente_ataca_a_un_zombi_que_no_es_peligroso_su_adrenalina_aumenta_en_20(self):
    morfeo = Sobreviviente(100)
    burgess = Zombi(0)
    self.assertEqual(morfeo.adrenalina, 120)
    
   def test_Si_un_sobreviviente_con_30_de_adrenalina_ataca_a_un_zombi_con_salud_inicial_40_su_salud_queda_en_25(self):
    morfeo = Sobreviviente(30)
    burgess = Zombi(40)
    self.assertEqual(burgess.salud, 25)
    
   def test_Si_un_sobreviviente_con_100_de_adrenalina_ataca_a_un_zombi_con_salud_inicial_30_su_salud_queda_en_0(self):
    morfeo = Sobreviviente(100)
    burgess = Zombi(30)
    self.assertEqual(burgess.salud, 0)
    
  # Que tire excepción cuando es un SuperZombi y cuando la salud de un zombi es > 500
  
   def test_Un_super_zombi_sabe_correr(self):
    gaiman = SuperZombi(100)
    self.assertTrue(milei.sabe_correr())
    
   def test_Un_super_zombi_sabe_regenerarse(self):
    gaiman = SuperZombi(0)
    gaiman.regenerarse()
    self.assertEqual(gaiman.salud, 100)
    
   def test_Si_un_super_zombi_con_salud_100_recibe_20_de_danio_su_salud_queda_en_40(self):
    gaiman = SuperZombi(100)
    gaiman.recibir_danio(20)
    self.assertEqual(gaiman.salud, 40)
  