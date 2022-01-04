
  def test_Si_creo_un_nuevo_Sobreviviente_le_puedo_especificar_su_adrenalina_inicial(self):
    sobreviviente = Sobreviviente(10)
    self.assertEqual(sobreviviente.adrenalina,10)
    
  def test_El_método_atacar_está_definido_en_la_clase_Sobreviviente(self):
    morfeo = Sobreviviente(100)
    self.assertTrue("atacar" in dir(morfeo) and callable(morfeo.atacar))
    
  def test_Si_un_sobreviviente_ataca_a_un_zombi_que_no_es_peligroso_su_adrenalina_aumenta_en_20(self):
    morfeo = Sobreviviente(100)
    burgess = Zombi(0)
    morfeo.atacar(burgess)
    self.assertEqual(morfeo.adrenalina, 120)
    
  def test_Si_un_sobreviviente_con_30_de_adrenalina_ataca_a_un_zombi_no_peligroso_lo_hace_con_15_de_daño(self):
    morfeo = Sobreviviente(30)
    burgess = Zombi(40)
    morfeo.atacar(burgess)
    self.assertEqual(burgess.hambre,  10)
    
  def test_Si_un_sobreviviente_con_40_de_adrenalina_ataca_a_un_zombi_no_peligroso_lo_hace_con_20_de_daño(self):
    morfeo = Sobreviviente(40)
    burgess = Zombi(48)
    morfeo.atacar(burgess)
    self.assertEqual(burgess.hambre,  8)
 
  def test_Un_sobreviviente_no_puede_atacar_a_un_zombi_peligroso(self):
    morfeo = Sobreviviente(40)
    burgess = Zombi(100)
    morfeo.atacar(burgess)
    self.assertEqual(burgess.hambre,  100)
 
def test_Un_sobreviviente_no_puede_atacar_a_un_super_zombi(self):
    morfeo = Sobreviviente(40)
    orfeo = SuperZombi(10)
    morfeo.atacar(orfeo)
    self.assertEqual(orfeo.hambre,  10)