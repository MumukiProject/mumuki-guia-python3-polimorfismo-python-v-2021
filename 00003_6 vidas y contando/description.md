Ahora que definimos el método `rehabilitar` en la clase `EstudianteDeVeterinaria`, podemos enviarle el mensaje, ¿no? :thinking:

Probémoslo escribiendo en orden en la consola:

```python
ムpelu = EstudianteDeVeterinaria()
```
```python
ムperez = Gato(30, 8)
```
```python
ムpelu.rehabilitar(perez)
```

Otra vez el código lanzó un error :cry:.
Esto es porque los gatos no comprenden el mensaje `recibir_rehabilitacion`. 

¡Solucionemos esto! :muscle:

> Definí en la clase `Gato` el método `recibir_rehabilitacion`. Cuando un gato recibe rehabilitación come 400 gramos de comida.