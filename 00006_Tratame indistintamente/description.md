¡Excelente! Ahora ya se puede `rehabilitar` a los tres tipos de animales que tenemos en nuestro sistema. Lo interesante es que cuando una instancia de `EstudianteDeVeterinaria` quiere `rehabilitar` a un animal, no pregunta de qué tipo es y en base a eso aplica la rehabilitación correspondiente, simplemente delega en el animal la responsabilidad de recibir la rehabilitación sin preocuparse por su clase. :relieved:

Esta capacidad de un objeto de poder enviarle el mismo mensaje indistintamente a objetos de distintas clases se llama **polimorfismo** y es uno de los ejes principales de la programación con objetos. :exploding_head:

> ¿Qué métodos nos permiten que alguien que estudia veterinaria rehabilite animales?