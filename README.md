# PROYECTO ECHIDNA BRICKS
Proyectos sobre Echidna y Bloques de construcción con el objetivo de realizar un kit que incluya bloques de construcción compatibles con LEGO y sensores y actuadores.

# Listado de Proyectos
1. [Gallo Despertador](./GalloDespertador/README.md)
2. [Estatuas musicales](./EstatuasMusicales/README.md)
3. [Helicóptero acelerómetro](./HelicopteroAcelerometro/README.md)
4. [Barrera automática](./BarreraAutomatica/README.md)
5. [Coche Teledirigido](./CocheTeledirigido/README.md)
6. [Rotografo](./Rotografo/README.md)
7. [Caja Fuerte](./CajaFuerte/README.md)
8. Puerta garaje
9. Tendedero

El objetivo es llegar a 10-15 proyectos

## Piezas usadas
El listado de piezas utilizadas en el proyecto es: [Piezas usadas](./Piezas_usadas.md) (también como hoja de cálculo: [Piezas_usadas.csv](./Piezas_usadas.csv))

Para cada pieza (Part ID + color) se indica:
- **Quantity**: la mayor cantidad usada en un mismo proyecto.
- **Total**: la suma de las cantidades usadas en todos los proyectos.

Ambos archivos se generan automáticamente a partir de los CSV de piezas de cada proyecto. Si se añade un proyecto nuevo o cambia algún CSV, hay que regenerarlos desde la raíz del repositorio con:

```bash
python3 scripts/piezas_usadas.py
```

No hay que editarlos a mano: los cambios se perderían al regenerarlos.

## Electrónica
[Electrónica](./Electronica/README.md) necesaria para desarrollar el proyecto: sensores, actuadores y cableado.
# Sensores y actuadores usados
| Proyecto | 1 Joystick | 2 Acel | 3 Puls | 4 LDR | 5 Micro | 6 Temp | 7 MkMk | 8 LEDs | 9 RGB | 10 Audio | 11 servo | 12 hum | 13 dist | LML |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Gallo Despertador](./GalloDespertador) | | | |X| | | | | | |X| | | |
| [Estatuas musicales](./EstatuasMusicales/) | | | | |X| | | | | |X| | | |
| [Helicóptero acelerómetro](./HelicopteroAcelerometro/) | |X| | | | | | | | |X| | | |
| [Barrera automática](./BarreraAutomatica/) | | | | | | | |X| | |X| |X| |
| [Coche Teledirigido](./CocheTeledirigido/) |X| | | | | | | | | |X| |X| |
| [Rotografo](./Rotografo/) | | |X| | | | | | | |X| | | |
| [Caja Fuerte](./CajaFuerte/) | | |X| | | | |X| | |X| | |X|
| Puerta garaje | | | | | | | | | | | | | | |
| Tendedero | | | | | | | | | | | | | | |

## Instrucciones de montaje
Programas usados:
- [LeoCAD](https://www.leocad.org/) para generar el diseño CAD.
- [LPub3D](https://trevorsandy.github.io/lpub3d/) para generar las instrucciones.

Para realizar las instrucciones de montaje tenemos la siguiente [guía de instalación de los programas](./guiaCAD/GuiaCAD.md)

## Documentacion de los proyectos
Cada uno de los proyectos queda documentado con la siguiente información:
- README explicación del proyecto y enlaces
- Montaje.pdf
- Archivo CAD de montaje.ldr
- CSV de piezas
- programa EchidnaML.sb3
- Gif animado montaje
- Imagen del proyecto


## Autores
El autor de los proyectos es Jorge Lobo.  


Colaboradores:   
- Xabier Rosas  
- Juan David Rodriguez  
- Jose Pujol
