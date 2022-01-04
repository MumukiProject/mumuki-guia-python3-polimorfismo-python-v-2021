
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_hambre_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.hambre,44)

  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_hambre_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.hambre,44)
    
  def test_Un_super_zombi_sabe_correr(self):
    gaiman = SuperZombi(100)
    self.assertTrue(gaiman.sabe_correr())
    
  def test_Un_super_zombi_sabe_regenerarse(self):
    gaiman = SuperZombi(0)
    gaiman.regenerarse()
    self.assertEqual(gaiman.hambre, 100)
    
  def test_Si_un_super_zombi_con_hambre_100_recibe_20_de_danio_su_hambre_queda_en_80(self):
    gaiman = SuperZombi(100)
    gaiman.recibir_danio(20)
    self.assertEqual(gaiman.hambre, 80)
    
  def test_Un_super_zombi_siempre_es_un_peligro(self):
    gaiman = SuperZombi(0)
    self.assertTrue(gaiman.es_un_peligro())
    
  def test_Un_zombi_sabe_correr(self):
    gaiman = Zombi(100)
    self.assertTrue(gaiman.sabe_correr())
    
  def test_Si_un_super_zombi_con_hambre_100_recibe_20_de_danio_su_hambre_queda_en_80(self):
    gaiman = SuperZombi(100)
    gaiman.recibir_danio(20)
    self.assertEqual(gaiman.hambre, 80)
    
  def test_Un_Zombi_es_un_peligro_si_tiene_más_de_50_de_hambre(self):
    gaiman = Zombi(51)
    self.assertTrue(gaiman.es_un_peligro())
    
  def test_Un_Zombi_no_es_un_peligro_si_tiene_50_de_hambre(self):
    gaiman = Zombi(50)
    self.assertFalse(gaiman.es_un_peligro())