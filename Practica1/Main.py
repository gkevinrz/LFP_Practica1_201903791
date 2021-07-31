class Principal:
    def __init__(self):
        self.prueba=3

    def MostrarConsola(self):
        print(' _______________________________\n'
        '|        Control de Notas       | \n'
        '|-------------------------------|\n'
        '| 1. Cargar Archivo             | \n'
        '| 2. Mostrar reporte en consola |\n'
        '| 3. Exportar reporte           |\n'
        '| 4. Salir                      |\n'
        '|_______________________________|')
        print('\n')
        print('Seleccione una opción: ')
        Opcion=int(input('> '))




P=Principal()
P.MostrarConsola()