from tkinter import filedialog,Tk
from tkinter.constants import NONE
from typing import List, Text


class Principal:
    def __init__(self):
        self.Promedio_Estudiantes=0
        self.TituloCurso=''
        self.ListaEstudiantes=[]
        self.ListaNotas=[]
        self.ListaAprobados=[]
        self.NotasReprobados=[]
        self.ListaReprobados=[]
        self.NotasAprobados=[]
        self.Notas_Maximas=[]
        self.Nota_Maxima=0
        self.Notas_Minimas=[]
        self.Nota_Minima=0
        self.ListaOrdenadaNotas=[]
        self.ListaNombresOrdenados=[]
        self.ListaReportes=[]

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
            self.CrearReporteHtml()
            self.MostrarConsola()
        else:
            print('Sesión Cerrada.')
    
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
        #print(self.array3)
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
        self.ReportesComas2=self.ReportesComas+','
        self.reportessincomas=[]
        self.r=''
        self.r2=''
        for x in self.ReportesComas2:
            if x!=',':
                self.r=self.r+x
            else:
                self.r2=self.r
                self.reportessincomas.append(self.r)
                self.r=''
        
        self.NotasEstudiantes=[]        
        print('Curso: '+ self.titulo)
        self.TituloCurso=self.titulo.replace('_',' ')
        for i in self.NotasEstudiante:
            self.NotasEstudiantes.append(round(float(i)))

        #print(self.NombreEstudiantes)
        #print(self.NotasEstudiantes)
        #print(self.ReportesComas)
        #print(self.reportessincomas) 
        ##################################
        self.ListaEstudiantes=self.NombreEstudiantes
        self.ListaNotas=self.NotasEstudiantes
        self.ListaReportes=self.reportessincomas
        ########################################
        for i in self.reportessincomas:
            if i=='DESC':
                self.OrdenamientoDESC(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='MAX':
                self.NotasMaximas(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='ASC':
                self.OrdenamientoASC(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='APR':
                self.Aprobados(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='REP':
                self.Reprobados(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='MIN':
                self.NotasMinimas(self.NotasEstudiantes,self.NombreEstudiantes)
            elif i=='AVG':
                self.Promedio(self.NotasEstudiantes)


        self.MostrarConsola()
    ###################33
    def OrdenamientoDESC(self,ListaNotas,ListaNombres):
        self.nombres=ListaNombres
        self.notas=ListaNotas
        for k in range(len(self.notas)-1):
            for x in range(len(self.notas)-1-k):
                if self.notas[x]<self.notas[x+1]:
                    aux1=self.notas[x]
                    self.notas[x]=self.notas[x+1]
                    self.notas[x+1]=aux1
                    aux2=self.nombres[x]
                    self.nombres[x]=self.nombres[x+1]
                    self.nombres[x+1]=aux2
        print('| Notas ordenadas descendentemente\n')
        for i in range(len(self.notas)):
            print(self.nombres[i]+' | ',self.notas[i])
            print('-------------------------------')
        print('')
        self.ListaNombresOrdenados=self.nombres
        self.ListaOrdenadaNotas=self.notas
    #################3
    def NotasMaximas(self,ListaNotas,ListaNombres):
        self.Nombres=ListaNombres
        self.Notas=ListaNotas      
        self.notamax=max(self.Notas)
        self.NombresMaximos=[]
        self.notaMaxima=[]
        for i in range(len(self.Notas)):
            if self.Notas[i]==self.notamax:
                self.NombresMaximos.append(self.Nombres[i])
        print('|     Notas Máximas  |\n')
        for x in range(len(self.NombresMaximos)):
            print(self.NombresMaximos[x]+' | ',self.notamax)
        self.Notas_Maximas=self.NombresMaximos
        self.Nota_Maxima=self.notamax

        print('')
   #########################
    def OrdenamientoASC(self,ListaNotas,ListaNombres):
        self.nombres2=ListaNombres
        self.notas2=ListaNotas
        for k in range(len(self.notas2)-1):
            for x in range(len(self.notas2)-1-k):
                if self.notas2[x]<self.notas2[x+1]:
                    aux1=self.notas2[x]
                    self.notas2[x]=self.notas2[x+1]
                    self.notas2[x+1]=aux1
                    aux2=self.nombres2[x]
                    self.nombres2[x]=self.nombres2[x+1]
                    self.nombres2[x+1]=aux2
            
        print('| Notas ordenadas ascendentemente\n')
        for i in range(len(self.notas2)-1,-1,-1):
            print(self.nombres2[i]+' | ',self.notas2[i])
            print('-------------------------------')
        print('')
        self.ListaNombresOrdenados=self.nombres2
        self.ListaOrdenadaNotas=self.notas2
############################
    def Aprobados(self,ListaNotas,ListaNombres):
        self.NotasApr1=ListaNotas
        self.NombresApr1=ListaNombres
        self.NotasApr2=[]
        self.NombresApr2=[]
        for l in range(len(self.NotasApr1)):
            if self.NotasApr1[l]>=61:
                self.NotasApr2.append(self.NotasApr1[l])
                self.NombresApr2.append(self.NombresApr1[l])
            
        print(' Estudiantes Aprobados: ',len(self.NotasApr2))
        print('')
        for i in range(len(self.NotasApr2)):
            print(self.NombresApr2[i]+' | ',self.NotasApr2[i])
            print('------------------------------------')
        self.NotasAprobados=self.NotasApr2
        self.ListaAprobados=self.NombresApr2

    def Reprobados(self,ListaNotas,ListaNombres):
        self.NotasRep1=ListaNotas
        self.NombresRep1=ListaNombres
        self.NotasRep2=[]
        self.NombresRep2=[]
        for l in range(len(self.NotasRep1)):
            if self.NotasRep1[l]<61:
                self.NotasRep2.append(self.NotasRep1[l])
                self.NombresRep2.append(self.NombresRep1[l])
            
        print(' Estudiantes Reprobados: ',len(self.NotasRep2))
        print('')
        for i in range(len(self.NotasRep2)):
            print(self.NombresRep2[i]+' | ',self.NotasRep2[i])
            print('------------------------------------')
        self.ListaReprobados=self.NombresRep2
        self.NotasReprobados=self.NotasRep2

    def NotasMinimas(self,ListaNotas,ListaNombres):
        self.NombresMin1=ListaNombres
        self.NotasMin1=ListaNotas      
        self.notamin=min(self.NotasMin1)
        self.NombresMinimos=[]
        for i in range(len(self.NotasMin1)):
            if self.NotasMin1[i]==self.notamin:
                self.NombresMinimos.append(self.NombresMin1[i])
        print('|     Notas Mínimas  |\n')
        for x in range(len(self.NombresMinimos)):
            print(self.NombresMinimos[x]+' | ',self.notamin)
        self.Notas_Minimas=self.NombresMinimos
        self.Nota_Minima=self.notamin
        print('')
    def Promedio(self,ListaNotas):
        self.NotasPromedio=ListaNotas
        self.Suma=0
        self.D=len(self.NotasPromedio)
        for i in self.NotasPromedio:
            self.Suma=self.Suma+i
        self.Promedio_Estudiantes=(self.Suma)/(self.D)
        print('El promedio de nota es: ', (self.Suma)/(self.D))
        print('')
        print('------------------------------------')
        

    def CrearReporteHtml(self):
        f = open ('Notas_Estudiantiles.html','w',encoding='UTF-8')
        cuerpo=f""" 
        <!DOCTYPE html>
        <html lang="en" >
        <head>
        <meta charset="UTF-8">
        <title>Reporte</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
        <link rel="stylesheet" href="./style.css">

        </head>
        <body>
        <!-- partial:index.partial.html -->
        <div class="skewed-bg">
	    <div class="content">
        <div id="Logo">
        <img src="./Img/Logo.png">
        </div>
		<h1 class="title">{self.TituloCurso}</h1>
         <p class="text">Reporte de notas estudiantiles</p>
	    </div>
        </div>
        <div class="Titulo">
        <h1>Listado de estudiantes</h1>
        </div>

        <!-- partial -->
        <div class="container">
    	<table>
		<thead>
			<tr>
				<th>Estudiante</th>
				<th>Nota</th>
				<th>Estado</th>
				
			</tr>
		</thead>
        <tbody>"""

        cuerpo2=''
        for i in range(len(self.ListaEstudiantes)):
            if self.ListaNotas[i]<61:
                cuerpo2+=f"""
                <tr>
                <td >{self.ListaEstudiantes[i]}</td> 
                <td style="background-color:red;color:white;">{self.ListaNotas[i]}</td>
                <td>Reprobado</td>
                </tr>
                """
            else:
                cuerpo2+=f"""
                <tr>
                <td >{self.ListaEstudiantes[i]}</td> 
                <td style="background-color: #2980b9 ;color:white;">{self.ListaNotas[i]}</td>
                <td>Aprobado</td>
                </tr>
                """

        cuerpo3="""
        </tbody>
        </table>
        </div>
        <div class="Titulo">
        <h1>Reportes</h1>
        </div>
        <div class="grid-container">
        """      
        cuerpo4=''
        for i in self.ListaReportes:
            if i=='ASC':
                cuerpo4+="""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
                Notas ordenadas ascendentemente
                <table>
	        	<thead>
		    	<tr>
				<th>Estudiante</th>
				<th>Nota</th>
		    	</tr>
	        	</thead>
		        <tbody>"""
                for i in range(len(self.ListaOrdenadaNotas)-1,-1,-1):
                    cuerpo4+=f"""
                    <tr>
				    <td>{self.ListaNombresOrdenados[i]}</td>
			        <td>{self.ListaOrdenadaNotas[i]}</td>
                    </tr>
                    """
                
                cuerpo4+="""
                </tbody>
            	</table>
                </div>"""
            elif i=='DESC':
                    
                cuerpo4+="""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
                Notas ordenadas descendentemente
                <table>
	        	<thead>
		    	<tr>
				<th>Estudiante</th>
				<th>Nota</th>
		    	</tr>
	        	</thead>
		        <tbody>"""
                for i in range(len(self.ListaOrdenadaNotas)):
                    cuerpo4+=f"""
                    <tr>
				    <td>{self.ListaNombresOrdenados[i]}</td>
			        <td>{self.ListaOrdenadaNotas[i]}</td>
                    </tr>
                    """
                
                cuerpo4+="""
                </tbody>
            	</table>
                </div>"""
            elif i=='MAX':
                
                cuerpo4+="""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
                Notas Máximas
                <table>
	        	<thead>
		    	<tr>
				<th>Estudiante</th>
				<th>Nota</th>
		    	</tr>
	        	</thead>
		        <tbody>"""
                for i in range(len(self.Notas_Maximas)):
                    cuerpo4+=f"""
                    <tr>
				    <td>{self.Notas_Maximas[i]}</td>
			        <td>{self.Nota_Maxima}</td>
                    </tr>
                    """
                
                cuerpo4+="""
                </tbody>
            	</table>
                </div>"""
            elif i=='MIN':
                cuerpo4+="""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
                Notas Mínimas
                <table>
	        	<thead>
		    	<tr>
				<th>Estudiante</th>
				<th>Nota</th>
		    	</tr>
	        	</thead>
		        <tbody>"""
                for i in range(len(self.Notas_Minimas)):
                    cuerpo4+=f"""
                    <tr>
				    <td>{self.Notas_Minimas[i]}</td>
			        <td>{self.Nota_Minima}</td>
                    </tr>
                    """
                
                cuerpo4+="""
                </tbody>
            	</table>
                </div>"""
            elif i=='APR':
                cuerpo4+=f"""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
              	Cantidad Aprobados : {len(self.ListaAprobados)}
                </div>"""
            elif i=='REP':
                cuerpo4+=f"""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
              	Cantidad Reprobados : {len(self.ListaReprobados)}
                </div>"""

            elif i=='AVG':
                cuerpo4+=f"""
                <div style="padding-top:40%;padding-bottom:60px;"class="grid-item"> 
              	El promedio de notas es: {self.Promedio_Estudiantes} 
                </div>"""

        cuerpon="""
        </body>
        </html>
        """

       
		
	   
        cuerpototal=cuerpo+cuerpo2+cuerpo3+cuerpo4+cuerpon
        f.write(cuerpototal)
        f.close()

P=Principal()
P.MostrarConsola()
