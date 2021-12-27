Los animales que programamos en la lección anterior ya saben `comer`, el tema es… ¿quién los alimenta?

Para resolver este problema vamos a modelar estudiantes de veterinaria que tienen la particularidad de no poseer atributos. Como consecuencia, esta va a ser la primera clase que definamos que no necesite constructor. Pero a no desesperar, esto no significa que no podamos instanciar estudiantes, simplemente no definiremos `__init__` ya que no es necesario inicializar atributos.

> Definí la clase `EstudianteDeVeterinaria` con el método `alimentar` que recibe un animal y la cantidad de gramos que tendrá que comer.