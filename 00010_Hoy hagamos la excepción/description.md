Bien, ya tenemos forma de `atacar` a los zombis. Sin embargo, hay algo que no tuvimos en cuenta :thinking:. Cuando enviemos el mensaje `atacar` a una instancia de la clase `Sobreviviente` sabemos que atacará al zombi solo si no es un peligro, pero ¿qué sucede en caso que no se produzca el ataque? :face_with_hand_over_mouth:

Lo ideal sería que tengamos una forma de enterarnos si el ataque se llevó a cabo o no, sobre todo teniendo en cuenta que el mensaje es `atacar` y no `atacar_si_es_posible`.  Una solución posible es cambiar el nombre de nuestro método y ya. Peeeero, tenemos una propuesta superadora, ¡lanzar una excepción! :collision:

En nuestro recorrido ya hemos visto muchas, por ejemplo al dividir por cero o al enviar un mensaje a un objeto que no lo entiende. Esas excepciones ya son parte del lenguaje y son indicaciones de que algo salió mal. Lo interesante es que podemos lanzar nuestras propias excepciones utilizando `raise` de la siguiente forma...

```python
ム raise Exception('Este es el mensaje de la excepción que estamos lanzando')
```

... y obtendremos lo siguiente:

```
File "<input>", line 1, in <module>
Exception: Este es el mensaje de la excepción que estamos lanzando
```

¡Veamos si se entendió!

> Modificá el método `atacar` para que en caso que no sea posible realizar el ataque lance una excepción con el mensaje `Es peligroso atacar a este zombi`.