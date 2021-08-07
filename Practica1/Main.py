from tkinter import filedialog,Tk
from tkinter.constants import NONE
from typing import Text


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
        if(Opcion==1):
            self.abrir2=self.Abrir()
            if self.abrir2==None:
                print('No se eligió archivo. Intente de nuevo')
                self.MostrarConsola()
            else:
                print('---------- Archivo de texto -------')
                print(self.abrir2)
                print("-------------------------------------")         
                self.MostrarConsola()
        elif(Opcion==2):
            self.QuitarSaltos(self.abrir2)

        elif(Opcion==3):
            print('Opcion3')
        else:
            print('Error. Opción no válida')
    
    def Abrir(self):
        #Tk().withdraw()
        ArchivoLFP=filedialog.askopenfile(initialdir='./',title='Seleccione una archivo .LFP',filetypes=(('Archivos .lfp','*.lfp'),('Todos los archivos','*.*')))
        if ArchivoLFP is None:
            return None
        else:   
            self.TextoLFP=ArchivoLFP.read()
            ArchivoLFP.close()     
            return self.TextoLFP
 
    def QuitarSaltos(self,texto):
        #self.array=texto.split('\n')
        self.array2=[]
        self.t=''
        #print(self.array)
        self.title=''
        for i in texto:
            if i=='\n':
                pass
            else:
                self.t=self.t+i

        self.indice=0
        self.contad=0
        while(self.t[self.indice]!='='):
            #self.contad=self.contad+1
           
            self.array2.append(self.t[self.indice])
            self.indice=self.indice+1
        #print(self.array2)
        self.titulo=''
        for s in self.array2:
            if s==' ':
                pass
            elif s=='=':
                pass
            else:
                self.titulo=self.titulo+s
        self.indice2=0
        #print(self.t)
        self.array3=[] #Array de Estudiantes y Notas
        self.array4=[] #Array de  comandos
        #for para estudiantes
        for x in self.t:
            if x=='<':
                self.indice2=self.t.index(x)
                while(self.t[self.indice2]!='}'):
                    self.array3.append(self.t[self.indice2])
                    self.indice2=self.indice2+1
                break
            else:
                pass
        #for para comandos
        self.indice3=0
        for y in self.t:
            if y=='}':
                self.indice3=self.t.index(y)
                while(self.indice3<len(self.t)):
                    self.array4.append(self.t[self.indice3])
                    self.indice3=self.indice3+1
            else:
                pass
        self.ArrayAuxEst=[]
        self.indice_st=0
        self.ts=''
##################################################3 
        for l in self.array3:
            if l=='<':
                pass
            elif l=='>':
                pass
            else:
                self.ts=self.ts+l
        self.ts2=''
        self.indice4=0
        self.indice5=0
        ##
        self.ts3=self.ts+','
        ##        
        while(self.indice4<len(self.ts3)):
            self.ts2=self.ts2+self.ts3[self.indice4]
            if self.ts3[self.indice4]==',':
                self.ArrayAuxEst.append(self.ts2)
                self.ts2=''
            self.indice4=self.indice4+1
        self.list2=[]
        self.listanombres1=[]
        for u in self.ArrayAuxEst:
            self.listaa=u.split(';')
            self.list2.append(self.listaa)
        self.Notas1=[]
        for elems in self.list2:
            self.Notas1.append(elems[1])
        for elems2 in self.list2:
            self.listanombres1.append(elems2[0])
        ##
        self.NombresComillas=[]
        for elemento3 in self.listanombres1:
            self.NombresComillas.append(elemento3.split('"'))
        #####
        self.NombreEstudiantes=[]
        for elemento4 in self.NombresComillas:
            if elemento4=='':
                pass
            else:
                self.NombreEstudiantes.append(elemento4[1])
        ##
        self.numerocomas=''
        for elementoNum in self.Notas1:
            for s in elementoNum:
                if s==' ':
                    pass
                else:
                    self.numerocomas=self.numerocomas+s
        ##          
        self.splitnotas=self.numerocomas.split(',')
        self.NotasEstudiante=[]
        for e in self.splitnotas:
            if e=='':
                pass
            else:
                self.NotasEstudiante.append(e)
        ##
        #reportes
        #
        self.ReportesComas=''
        for elementos in self.array4:
            if elementos==' ':
                pass
            elif elementos=='}':
                pass
            else:
                self.ReportesComas=self.ReportesComas+elementos
        
        print(self.titulo)
        print(self.NotasEstudiante)
        print(self.NombreEstudiantes)
        print(self.ReportesComas)

P=Principal()
P.MostrarConsola()