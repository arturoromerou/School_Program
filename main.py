from conn import ConexionMDB
import atributos_conexion as acx
import os
import sys
############## CONEXION CON LA BD ##############
def main():
    cx = ConexionMDB(
        acx.CADENA_CONEXION,
        acx.BASE_DATOS,
        acx.ALUMNOS,
        acx.PROFESORES
    )
    menu_administrador(cx)

############## AGREGAR ALUMNOS A LA BD ##############
def insert_student(cx):
    os.system("clear")
    continuar = True
    while continuar:
        student_name = input("Nombres del Estudiante: ")
        student_last = input("Apellidos del Estudiante: ")
        student_age = input("Edad del Estudiante: ")

        nuevo_st = cx.insertar_alumnos(
            {
                "nombre": (student_name),
                "apellido": (student_last),
                "edad": (student_age),
                "es_visible": True
            }
        )
        print(f"se agrego satisfactoriamnete el alumno {student_name} con el id ", nuevo_st)

        print("\n********************\n")
        print('Desea agregar otro Estudiante? [s] [n]')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        opcion = opcion.lower()

        if opcion == "s":
            continuar = True
            os.system("clear")
        elif opcion == "n":
            continuar = False
            os.system("clear")
            
############## AGREGAR PROFESORES A LA BD ##############
def insert_teacher(cx):
    os.system("clear")
    continuar = True
    while continuar:
        teacher_name = input("Nombres del Profesor: ")
        teacher_last = input("Apellidos del Profesor: ")
        teacher_age = input("Edad del Profesor: ")

        nuevo_pf = cx.insertar_profesor(
            {
                "nombre": (teacher_name),
                "apellido": (teacher_last),
                "edad": (teacher_age),
                "es_visible": True
            }
        )
        print(f"se agrego satisfactoriamnete el alumno {teacher_name} con el id ", nuevo_pf)

        print("\n********************\n")
        print('Desea agregar otro Profesor? [s] [n]')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        opcion = opcion.lower()

        if opcion == "s":
            continuar = True
            os.system("clear")
        elif opcion == "n":
            continuar = False
            os.system("clear")

###################### MENU ADMINISTRADOR #######################        
def menu_administrador(cx):
    os.system("clear")
    continuar = True
    while continuar:
        print("\n********** ADMINISTRADOR **********\n")
        print('[1] Agregar Estudiantes')
        print('[2] Agregar Profesores')
        print('[3] Modificar estudiantes en el sistema')
        print('[4] Eliminar estudiantes del sistema')
        print('\n[s] Salir del sistema')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        

        if opcion == "1":
            insert_student(cx)
        elif opcion == "2":
            insert_teacher(cx)
        #elif opcion == "3":
        #    #modificar_articulo_almacen(conexion_pg)
        #elif opcion == "4":
        #    #eliminar_articulo(conexion_pg)
        elif opcion == "s":
            sys.exit()
        #elif opcion == "b":
        #    #menu_comprador(conexion_pg)
        #else:
        #    opcion == input("elija una seleccion valida: ")


main()