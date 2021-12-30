  
  def test_El_método_recibir_rehabilitacion_está_definido_en_la_clase_Caballo(self):
    nano = Caballo(0,'Cuarto de Milla')
    self.assertTrue("recibir_rehabilitacion" in dir(nano) and callable(nano.recibir_rehabilitacion))
    
  def test_Cuando_un_Caballo_recibe_rehabilitación_galopa_3_km_come_3000_gramos_de_comida_y_vuelve_a_galopar_5_km(self):
    nano = Caballo(1000,'Cuarto de Milla')
    nano.recibir_rehabilitacion()
    self.assertEqual(nano.energia,60992)
    
  
  def test_El_método_recibir_rehabilitacion_está_definido_en_la_clase_Golondrina(self):
    norita = Golondrina(0,'General las Heras')
    self.assertTrue("recibir_rehabilitacion" in dir(norita) and callable(norita.recibir_rehabilitacion))
    
  def test_Cuando_una_golondrina_recibe_rehabilitación_vuela_hacia_Lihuel_Calel(self):
    norita = Golondrina(100,'General Las Heras')
    norita.recibir_rehabilitacion()
    self.assertEqual(norita.ciudad, "Lihuel Calel")  
    
  