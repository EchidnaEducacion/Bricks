#!/usr/bin/env python3
"""Genera Piezas_usadas.csv y Piezas_usadas.md a partir de los CSV de piezas de cada proyecto.

Uso (desde cualquier directorio):
    python3 scripts/piezas_usadas.py

Cada combinación Part ID + Color Code es una pieza distinta.
- Quantity: mayor cantidad usada en un mismo proyecto.
- Total: suma de las cantidades usadas en todos los proyectos.
"""
import csv
import glob
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CABECERA = ["Part Name", "Color", "Quantity", "Total", "Part ID", "Color Code"]


def leer_piezas():
    piezas = {}
    nombres_por_id = {}
    suma_origen = 0
    for ruta in sorted(glob.glob(os.path.join(RAIZ, "*", "*.csv"))):
        with open(ruta, encoding="utf-8", newline="") as f:
            for fila in csv.DictReader(f):
                cantidad = int(fila["Quantity"])
                suma_origen += cantidad
                nombre = re.sub(r"\s+", " ", fila["Part Name"]).strip()
                part_id = fila["Part ID"]
                if nombre != part_id:
                    nombres_por_id.setdefault(part_id, nombre)
                clave = (part_id, int(fila["Color Code"]))
                pieza = piezas.setdefault(
                    clave, {"nombre": nombre, "color": fila["Color"], "max": 0, "total": 0}
                )
                pieza["max"] = max(pieza["max"], cantidad)
                pieza["total"] += cantidad
    # Algunos CSV traen como nombre el propio Part ID (p. ej. geekservo1.dat)
    for (part_id, _), pieza in piezas.items():
        if pieza["nombre"] == part_id:
            pieza["nombre"] = nombres_por_id.get(part_id, part_id)
    return piezas, suma_origen


def filas(piezas):
    for (part_id, color_code), p in sorted(piezas.items()):
        yield [p["nombre"], p["color"], p["max"], p["total"], part_id, color_code]


def escribir_csv(piezas):
    # Mismo estilo que los CSV de los proyectos: cabecera sin comillas,
    # nombre y color entre comillas, resto sin comillas
    def entre_comillas(texto):
        return '"' + texto.replace('"', '""') + '"'

    with open(os.path.join(RAIZ, "Piezas_usadas.csv"), "w", encoding="utf-8", newline="") as f:
        f.write(",".join(CABECERA) + "\n")
        for nombre, color, *resto in filas(piezas):
            valores = [entre_comillas(nombre), entre_comillas(color)] + [str(v) for v in resto]
            f.write(",".join(valores) + "\n")


def escribir_md(piezas, total):
    lineas = [
        "# Piezas usadas",
        "",
        "Listado unificado de las piezas de todos los proyectos, generado a partir de los CSV de cada proyecto.",
        "",
        "- **Quantity**: mayor cantidad usada en un mismo proyecto.",
        "- **Total**: suma de las cantidades usadas en todos los proyectos.",
        "",
        "Descarga como hoja de cálculo: [Piezas_usadas.csv](./Piezas_usadas.csv)",
        "",
        "| " + " | ".join(CABECERA) + " |",
        "|---|---|---:|---:|---|---:|",
    ]
    lineas += ["| " + " | ".join(str(v) for v in fila) + " |" for fila in filas(piezas)]
    lineas += [
        "",
        f"**{len(piezas)} piezas distintas, {total} piezas en total.**",
        "",
        "> Archivo generado con `python3 scripts/piezas_usadas.py`. No editar a mano.",
        "",
    ]
    with open(os.path.join(RAIZ, "Piezas_usadas.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))


def main():
    piezas, suma_origen = leer_piezas()
    total = sum(p["total"] for p in piezas.values())
    assert total == suma_origen, "La suma de Total no coincide con los CSV de origen"
    escribir_csv(piezas)
    escribir_md(piezas, total)
    print(f"{len(piezas)} piezas distintas, {total} piezas en total")


if __name__ == "__main__":
    main()
