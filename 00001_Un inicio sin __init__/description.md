Los animales que programamos en la lección anterior ya saben `comer`, el tema es… ¿quién los alimenta? :flushed:

Para resolver este problema vamos a modelar estudiantes de veterinaria que tienen la particularidad de no poseer atributos. Como consecuencia, esta va a ser la primera clase que definamos que no necesite constructor. Pero a no desesperar, esto no significa que no podamos instanciar estudiantes, simplemente no definiremos `__init__` ya que no es necesario inicializar atributos. :relieved:

Esto cambia levemente nuestro diagrama que será así:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-polimorfismo-python-v-2021/master/assets/clases_3_1647535903078.1.svg" alt="clases_3_1647535903078.1.svg" width="300px" height="auto">

> Definí la clase `EstudianteDeVeterinaria` con el método `alimentar` que recibe un animal y la cantidad de gramos que tendrá que comer.