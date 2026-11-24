# 1. CLASE EMPRESA

class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.empleados = []
        self.proyectos = []

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def agregarProyecto(self, proyecto):
        self.proyectos.append(proyecto)


# 2. CLASE EMPLEADO

class Empleado:
    def __init__(self, nombre, identificacion, salario):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__salario = salario

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getSalario(self):
        return self.__salario

    def setSalario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f"{self.__nombre} - {self.__identificacion} - ${self.__salario}"


# 3. CLASE DESARROLLADOR

class Desarrollador(Empleado):
    def __init__(self, nombre, identificacion, salario, lenguaje):
        super().__init__(nombre, identificacion, salario)
        self.__lenguaje = lenguaje

    def getLenguaje(self):
        return self.__lenguaje

    def setLenguaje(self, lenguaje):
        self.__lenguaje = lenguaje

    def __str__(self):
        return super().__str__() + f" - {self.__lenguaje}"


# 4. CLASE LIDER DE PROYECTO

class LiderProyecto(Empleado):
    def __init__(self, nombre, identificacion, salario, experiencia):
        super().__init__(nombre, identificacion, salario)
        self.__experiencia = experiencia

    def getExperiencia(self):
        return self.__experiencia

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def __str__(self):
        return super().__str__() + f" - {self.__experiencia} años de experiencia"


# 5. CLASE PROYECTO

class Proyecto:
    def __init__(self, nombre, lider):
        self.__nombre = nombre
        self.lider = lider
        self.tareas = []

    def getNombre(self):
        return self.__nombre

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def __str__(self):
        return f"{self.__nombre} - Lider: {self.lider.getNombre()}"


# 6. CLASE TAREA

class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__estado = "Pendiente"

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"{self.__descripcion} - {self.__estado}"


# PROGRAMA PRINCIPAL

empresa = Empresa("Software Colombia")

lider = LiderProyecto("Carlos", "1001", 3000000, 5)

desarrollador = Desarrollador("Andres", "1002", 2000000, "Python")

empresa.agregarEmpleado(lider)
empresa.agregarEmpleado(desarrollador)

proyecto = Proyecto("Sistema de ventas", lider)

empresa.agregarProyecto(proyecto)

opcion = ""

while opcion != "6":

    print("\n===== MENU PRINCIPAL =====")
    print("1. Mostrar empleados")
    print("2. Mostrar proyectos")
    print("3. Agregar tarea")
    print("4. Mostrar tareas")
    print("5. Completar tarea")
    print("6. Guardar y salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("\nEMPLEADOS")

        for empleado in empresa.empleados:
            print(empleado)

    elif opcion == "2":
        print("\nPROYECTOS")

        for p in empresa.proyectos:
            print(p)

    elif opcion == "3":
        descripcion = input("Descripcion de la tarea: ")

        tarea = Tarea(descripcion)
        proyecto.agregarTarea(tarea)

        print("Tarea registrada correctamente")

    elif opcion == "4":
        print("\nLISTA DE TAREAS")

        for i in range(len(proyecto.tareas)):
            print(i + 1, proyecto.tareas[i])

        if len(proyecto.tareas) == 0:
            print("No hay tareas registradas")

    elif opcion == "5":

        for i in range(len(proyecto.tareas)):
            print(i + 1, proyecto.tareas[i])

        if len(proyecto.tareas) > 0:

            numero = input("Numero de la tarea: ")

            if numero.isdigit():
                numero = int(numero)

                if 1 <= numero <= len(proyecto.tareas):
                    proyecto.tareas[numero - 1].setEstado("Completada")
                    print("Tarea completada correctamente")
                else:
                    print("La tarea no existe")

            else:
                print("Ingrese un numero valido")

        else:
            print("No hay tareas registradas")

    elif opcion == "6":

        archivo = open("proyecto.txt", "w", encoding="utf-8")

        archivo.write("PROYECTO\n")
        archivo.write(str(proyecto) + "\n")

        archivo.write("\nEMPLEADOS\n")

        for empleado in empresa.empleados:
            archivo.write(str(empleado) + "\n")

        archivo.write("\nTAREAS\n")

        for tarea in proyecto.tareas:
            archivo.write(str(tarea) + "\n")

        archivo.close()

        print("Informacion guardada correctamente")
        print("Fin del programa")

    else:
        print("Opcion incorrecta")