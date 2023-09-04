#!/usr/bin/env python3
#craeted by: 1LugarParaProgramar
from time import sleep
from colorama import init, Fore, Style
init()
print(Fore.CYAN+Style.BRIGHT+"""

'########::'########:::'#######::'##::::'##:'##### ###:'########::'####::'#######:::'######::
 ##.... ##: ##.... ##:'##.... ##: ###::'###: ##.....:: ##. ... ##:. ##::'##.... ##:'##... ##:
 ##:::: ##: ##:::: ##: ##:::: ##: ####'####: ##::::::: ##:: :: ##:: ##:: ##:::: ##: ##:::...::
 ########:: ########:: ##:::: ##: ## ### ##: ######::: ##:: :: ##:: ##:: ##:::: ##:. ######::
 ##.....::: ##.. ##::: ##:::: ##: ##. #: ##: ##...:::: ##:::: ##:: ##:: ##:::: ##::..... ##:
 ##:::::::: ##::. ##:: ##:::: ##: ##:.:: ##: ##::::::: ##:::: ##:: ##:: ##::: : ##:'##::: ##:
 ##:::::::: ##:::. ##:. #######:: ##:::: ##: ########: ########::'####:. #######::. ######::
..::::::::::..::::::..:::.......:::..:::::..::...... ..::..........:::....:::.......::::......:::
  """)
info = """
    Script: Para sacar promedios de alumnos
        
    1LugarParaProgramar
    
    Created by: Hans saldias\n\n"""
for i in info:
    print(i, end="", flush=True)
    sleep(0.1)
alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno \n('salir') para finalizar): ")
    if nombre.lower() == 'salir':
        break

    notas = []
    while True:
        try:
            nota_str = input("\nIngrese una nota del alumno (o 'fin' para terminar): ")
            if nota_str.lower() == 'fin':
                break
            nota = float(nota_str)
            notas.append(nota)
        except ValueError:
            print("intente nuevamente eje: 6.5")

    promedio = sum(notas) / len(notas)
    alumno = {'nombre': nombre, 'notas': notas, 'promedio': promedio}
    alumnos.append(alumno)

print("\nLista de alumnos:")
for alumno in alumnos:
    print(f"\nNombre: {alumno['nombre']}, Promedio: {alumno['promedio']}")
    
p = input("\nDesea guardar en archivo.txt ? (s/n): ").lower()
if p == "s":
    with open("promedios.txt", 'a') as con:
        con.write(f"\nNombre: {alumno['nombre']}, Promedio: {alumno['promedio']}\n\n")
        print("Guardado exitosamente")
elif p == "n":
    print("Gracias Atte: 1LugarParaProgramar ")        
else:
    print("No se pudo Guardar, intente nuevamente")