
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_hambre_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.hambre,44)

  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_hambre_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.hambre,44)
    
  def test_Un_super_zombi_sabe_correr(self):
    gaiman = SuperZombi(100)
    self.assertTrue(milei.sabe_correr())
    
  def test_Un_super_zombi_sabe_regenerarse(self):
    gaiman = SuperZombi(0)
    gaiman.regenerarse()
    self.assertEqual(gaiman.hambre, 100)
    
  def test_Si_un_super_zombi_con_hambre_100_recibe_20_de_danio_su_hambre_queda_en_80(self):
    gaiman = SuperZombi(100)
    gaiman.recibir_danio(20)
    self.assertEqual(gaiman.hambre, 80)