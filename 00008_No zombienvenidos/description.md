Que lindos los animalitos, ¿qué bello dominio nos esperará a partir de ahora? :hugging:

¡Esperen! ¿Qué es ese ruido? AAAHHHHH :scream:

¡Menos mal que les dimos el alta a los animales para que escapen! Ahora tenemos que lidiar con una invasión zombi. :zombie: :woman_zombie:

Para ello vamos a definir dos clases, `Zombi` y `SuperZombi`. De ellas sabemos que:

* ambas tienen un atributo `hambre`;
* ambos tipos de zombis saben correr;
* los super zombis son siempre un peligro, mientras que los zombis solo si tienen más de 50 de `hambre`;
* los zombis no saben `regenerarse`;
* los super zombis pasan a tener 100 de `hambre` al recibir el mensaje `regenerarse`;
* ambos tipos de zombis pueden `recibir_danio` con una cantidad de daño recibida como argumento. Al hacerlo, disminuye su `hambre`. En el caso de los super zombis disminuye la cantidad recibida y en el de los zombis el doble de esa cantidad.

> * Definí las clases `Zombi` y `SuperZombi`.
> * Definí los métodos `sabe_correr`, `es_un_peligro`, `recibir_danio` y `regenerarse` donde correspondan.
> * Definí el constructor en cada una que permita dar un valor inicial al `hambre`.
