#Programa para cambiar los colores predeterminados de GTK
#gtkColors es la plantilla de donde va a sacar los colores que puede cambiar
#Programado por Juan Manuel Schillaci <ska@linux.org.ar> <jmschillaci@gmail.com>
#

from string import *
import os
class gtkRcCompose:
    def __init__(self, datos={}):
        self.datos = datos
        self.homeUser = "/home/" + os.environ["USER"]
        pass

    def getGtkRc(self):
        """
        Se le pasa un diccionario con los colores a usar por gtk
        """
        datos = self.datos 
        #Estos datos son de prueba
        homeUser=self.homeUser 
        
        #Si hay algun problema con el archivo por ejemplo si fue toqueteado a manopla, se lo generara de nuevo
        #try:
        #    plantillaColores = open(ubicacionGtkRc)
        #except:
        #    plantillaColores = open("gtkColors.rc")
        
        #plantilla = plantillaColores.read()
        #plantillaColores.close()
        header = "style \"mydefault\"\n{"
        footer = "}\nclass \"*\" style \"mydefault\""

        #Deberia hacer una lista de los valores posibles y que chequee contra este antes de querer hacer nada

        plantilla="" 
        for elem in datos.items():
            tipo = elem[0].split("_")
            tipo[0] = tipo[0].lower()
            plantilla += "\n" + tipo[0] + "[" + tipo[1] + "] = \"" + elem[1] + "\""
    
            
        #Ahora se guarda la plantilla resultante en la clase
        #self.fileContent = plantilla       
        self.fileContent = header + plantilla + "\n" + footer
        print "El archivo queda de la siguiente manera:: \n",self.fileContent 
    
    def guardar(self):
        """
        Escribe el string gtkrc generado en el gtkrc del usuario que lo llamo(al menos que se le especifique otra ubicacion en self.homeUser)
        """        
        homeUser = self.homeUser
        ubicacionGtkRc = homeUser + "/.gtkrc-2.0"
        #Ahora escribo el gtkrc
        gtkrcFile=open(ubicacionGtkRc, "w+")
        gtkrcFile.write(self.fileContent)
        gtkrcFile.close()
        pass    

    def createGtkRc(self):
        """
        Crea un archivo gtkrc vacio para el usuario reemplazando cualquiera que exista
        """
        self.getGtkRc()
        self.guardar()        

def prueba():
    datos = {}
    datos["FG_NORMAL"] = "#000000" 
    datos["FG_ACTIVE"]= "#000000"
    datos["FG_PRELIGHT"]= "#000000"
    datos["FG_SELECTED"]= "#F5F5F5"
    datos["FG_INSENSITIVE"]= "#747474"
    
    datos["BG_NORMAL"]= "#CCCCCC"
    datos["BG_ACTIVE"] = "#CCCCC0"
    datos["BG_PRELIGHT"]= "#DDDDD0"
    datos["BG_SELECTED"]= "#5f7ca8"
    datos["BG_INSENSITIVE"]= "#D6D6D6"
    
    datos["BASE_NORMAL"]= "#F5F5F5"
    datos["BASE_ACTIVE"]= "#bbbbb0"
    datos["BASE_PRELIGHT"]= "#bbbbb0"
    datos["BASE_SELECTED"]= "#5f7ca8"
    datos["BASE_INSENSITIVE"]= "#E9E9E9"
    
    datos["TEXT_NORMAL"]= "#000000"
    datos["TEXT_ACTIVE"]= "#f5f5f5"
    datos["TEXT_PRELIGHT"]= "#f5f5f5"
    datos["TEXT_SELECTED"]= "#f5f5f5"
    datos["TEXT_INSENSITIVE"]= "#747474"
    
    #Llamo a gtkRc y le paso un diccionario con los colores
    comp = gtkRcCompose(datos)
    comp.createGtkRc()

if __name__ == "__main__":
    prueba()
