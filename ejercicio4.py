import os

class Persona():
    def __init__(self):
        self.__perso = {}
        self.__ListaPersona = []

    def agregarpersona(self, cedula, nombre, apellidos, direccion, telefono):
        self.__perso = {
            'cedula': cedula,
            'nombre': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
        }
        self.__ListaPersona.append(self.__perso)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.__devengado ={}
        self.__deducciones ={}
        self.__ListaEmpleado =[]

    def agregarempleado(self):
        cedula = input("digite la cedula ..")
        nombre = input("digite el nombre ..")
        apellidos = input("digite los apellidos ..")
        direccion = input("digite la direccion")
        telefono = input("digite el telefono ..")
        salario = float(input("digite el salario"))

        per ={
            'cedula': cedula,
            'nombre': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
        }

        self.__devengado = {
            'salario' : salario,
            'alimentacion': 0,
            'transporte' : 0
        }

        self.__deducciones = {
            'salud' : 0,
            'pension': 0
        }
        
        super().agregarpersona(cedula, nombre, apellidos, direccion, telefono, salario)

        self.__ListaEmpleado.append([{"persona": per}, {"devengado": self.__devengado},{"deducciones": self.__deducciones}])

    def calculardevengado(self):
        self.__devengado['alimentacion'] = 80000
        self.__devengado['transporte'] = 60000
        

    def calculardeducciones(self):
        if self.__deducciones['salud'] == self.__devengado['salario'] * 4 / 1000:
            self.__deducciones['pension'] = self.__devengado['salario'] * 3.375 / 100


    def menu(self, opciones):
        while(True):
            os.system("clear")
            for item in range(len(opciones)):
                print(opciones[item]) 

            opcion = input("digite una opcion correcta: ")

            if opcion == "1":
                os.system("clear")
                self.agregarempleado()
                self.calculardevengado()
                self.calculardeducciones()

            elif opcion == "2":
                os.system("clear")
                print(self.__ListaEmpleado)
                input("digite una tecla para continuar ...")


def menuprincipal():
    os.system("clear")
    opciones = {
        "MENU PRINCIPAL",
        "1. ADICIONAR EMPLEADO",
        "2. MOSTRAR EMPELADO",
        "3. ELMINAR EMPLEADO",
        "4. SALIR ",
    }

    emp = Empleado()
    emp.menu(opciones)



def main():
    menuprincipal()


if __name__ == "__main__":
    main() 