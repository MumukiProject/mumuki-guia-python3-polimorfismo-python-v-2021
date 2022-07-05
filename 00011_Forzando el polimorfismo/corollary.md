Lo que acabamos de hacer al definir el método `recibir_danio` con un parámetro que no vamos a utilizar es forzar el polimorfismo.

Quizás parece innecesario ponerlo pero si no lo hiciéramos no serían polimórficas con los zombis y super zombis, ya que aunque dos métodos tengan el mismo nombre pero con distinta cantidad de parámetros, no es el mismo.

Esto traería como consecuencia que habría que definir en `Sobreviviente` un método que solo sirva para atacar plantas carnívoras zombis. :thumbsdown: