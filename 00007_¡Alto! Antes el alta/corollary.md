¡Excelente! :tada:

Con estos nuevos métodos nuestro diagrama quedará así:

DIAGRAMA DE CLASES

Dos cosas a remarcar del mismo:

* hay una flecha de línea punteada y punta abierta que conecta a la clase `EstudianteDeVeterinaria` con la interfaz `Animal`. Esta flecha representa que la clase utiliza a esta interfaz, en este caso como parámetro;
* los mensajes `recibir_rehabilitacion` y `esta_feliz` los ponemos directamente en la interfaz porque lo entienden todos los animales.

Lo importante acá es que le preguntamos al animal que recibimos como argumento si `esta_feliz` y no nos metimos directamente a ver los valores de sus atributos. Esto lo logramos gracias al ya mencionado polimorfismo. :raised_hands:

Esta práctica de minimizar el acceso a los atributos de otros objetos se llama **encapsulamiento** y a lo largo de nuestro recorrido fomentaremos que se respete el mismo. :nerd: