Teniendo en cuenta que nuestro diagrama de clases ahora es el siguiente:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-polimorfismo-python-v-2021/master/assets/clases_3_1647536154898.2.svg" alt="clases_3_1647536154898.2.svg" width="300px" height="auto">

¿Qué pasará si le enviamos el mensaje `rehabilitar` a una instancia de la clase `EstudianteDeVeterinaria`? :thinking:

Podés probarlo escribiendo lo siguiente en la consola:

```python
ム pelu = EstudianteDeVeterinaria()
ム perez = Gato(30, 8)
ム pelu.rehabilitar(perez)
```