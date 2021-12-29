
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_adrenalina_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.adrenalina,44)
    

  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_adrenalina_inicial(self):
    superZombi = SuperZombiZombi(44)
    self.assertEqual(superZombi.adrenalina,44)
    
  def test_Si_creo_un_nuevo_Sobreviviente_le_puedo_especificar_su_salud_inicial(self):
    sobreviviente = Sobreviviente(10)
    self.assertEqual(sobreviviente.salud,10)