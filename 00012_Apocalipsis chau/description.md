Por suerte el equipo de sobrevivientes pudo frenar el apocalipsis zombi. El problema es que quedaron con hambre, ¡solucionémoslo!

Para ello cambiemos de escenario y vayamos a un restaurante :pizza:. En este peculiar restaurante de comida italiana se dan algunos conflictos porque al equipo de chefs les gusta mucho lo picante y a sus ayudantes no tanto. :flag_it:

Del equipo de cocina sabemos que:

* cada chef tiene un atributo `plato_del_dia`;
* las instancias de `Chef` pueden `picantear` ese plato solo si **no** está demasiado picante, en caso de estarlo arrojan una excepción que dice `El plato ya está demasiado picante`; 
* las instancias de `AyudanteDeCocina` no tienen atributos ya que pueden `suavizar` cualquier plato que reciban como argumento.

Mientras que de los platos podemos contar lo siguiente:

* las `Pasta`s tienen un atributo `ajies` que inicialmente es 0;
* están demasiado picantes cuando tienen más de 10 `ajies`;
* al ser picanteadas aumenta en 5 su cantidad de `ajies` y al ser suavizadas pierden 1;
* las `Pizza`s tienen `condimento` que inicialmente es `"adobo"`;
* se considera que una pizza está demasiado picante si su condimento es `"cayena"`;
* al suavizar una pizza su condimento pasa a ser `"orégano"` y al picantearla, `"cayena"`.
* Los constructores en ambos platos solo deben tener `self` como parámetro porque sus atributos siempre se inicializan con el mismo valor. :hot_pepper:

> Definí las clases necesarias para poder hacer lo siguiente:
>
```python
fideos = Pasta()
muzzarella = Pizza()
jor = Chef(fideos)
luchi = AyudanteDeCocina()
jor.picantear()
luchi.suavizar(fideos)
jor.plato_del_dia = muzzarella
luchi.suavizar(muzzarella)
jor.picantear()
```