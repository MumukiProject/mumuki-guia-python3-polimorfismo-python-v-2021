Los objetos polimórficos deben pertenecer a clases que entiendan un mismo mensaje más allá de cómo esté definido el método, es decir, dos o más objetos son polimórficos cuando sus clases comparten una interfaz. 

Si bien esta interfaz no se refleja a nivel código sí puede hacerse a nivel diagrama de clases. Para ello hay que hacer dos cosas:

* darle un nombre a la interfaz, en este caso la llamaremos `Animal`, ya que `Caballo`, `Golondrina` y `Gato` son animales. Distinguiremos a las interfaces de las clases agregando `(I)` a las primeras;
* y conectar cada clase a la interfaz que implementa. Para esto utilizamos una flecha con línea punteada y punta cerrada:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-polimorfismo-python-v-2021/master/assets/clases_3_1648655538771.6.svg" alt="clases_3_1648655538771.6.svg" width="800" height="auto">


Para que estemos ante un caso de **polimorfismo** es necesaria la presencia de al menos tres objetos: uno que envíe el mensaje y dos de clases distintas que puedan entenderlo. :exploding_head: