Como si no fuera suficiente tener zombis y super zombis, ahora se suman a este escenario catastrófico las temibles ¡plantas carnívoras zombis! :bamboo:

De ellas sabemos que:

* tienen un atributo `clorofila`;
* son un peligro cuando dicho atributo es mayor a 40;
* saben `hacer_fotosintesis` por un tiempo, lo cual aumenta su `clorofila` en esa cantidad de tiempo;
* cuando reciben daño, su `clorofila` disminuye 10 unidades.

:warning: Es importante tener en cuenta que si bien las plantas carnívoras zombis disminuyen siempre la misma cantidad de clorofila al recibir daño, deben ser polimórficas con los zombis y los super zombis por lo que es necesario que ese método tenga los mismos parámetros.

> Definí la clase `PlantaCarnivoraZombi` con su constructor y los métodos `es_un_peligro`, `hacer_fotosintesis` y `recibir_danio`.