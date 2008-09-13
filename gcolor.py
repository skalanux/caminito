#!/usr/bin/env python
    
#----------------------------------------------------------------------
# gcolor.py
# Juan Manuel Schillaci 
# 08/05/2005
#----------------------------------------------------------------------

import sys
import cambiarcolores
import string
from GladeWindow import *

#----------------------------------------------------------------------

class gcolor(GladeWindow):

    #----------------------------------------------------------------------

    def __init__(self):

        ''' '''
        self.init()

    #----------------------------------------------------------------------

    def init(self):

        filename = 'gcolorchange.glade'

        widget_list = [
            'principal',
            'btn_cancelar',
            'btn_aplicar',
            'btn_reset',
            'FG_NORMAL',
            'FG_ACTIVE',
            'FG_PRELIGHT',
            'FG_SELECTED',
            'FG_INSENSITIVE',
            'BG_NORMAL',
            'BG_ACTIVE',
            'BG_PRELIGHT',
            'BG_SELECTED',
            'BG_INSENSITIVE',
            'BASE_NORMAL',
            'BASE_ACTIVE',
            'BASE_PRELIGHT',
            'BASE_SELECTED',
            'BASE_INSENSITIVE',
            'TEXT_NORMAL',
            'TEXT_ACTIVE',
            'TEXT_PRELIGHT',
            'TEXT_SELECTED',
            'TEXT_INSENSITIVE',
            ]

        handlers = [
            'on_btn_cancelar_clicked',
            'on_btn_aplicar_clicked',
            'on_btn_resetear_clicked',
            ]

        top_window = 'principal'
        GladeWindow.__init__(self, filename, top_window, widget_list, handlers)
        datos=self.getMapaActual(formato="gdcolor")
        self.inicializarControles(datos)

        #Ver la url http://www.pygtk.org/pygtk2reference/class-gtkstyle.html que esta explicado que 
        #fg, bg, etc son constantes para los nuevos widgets
    
    def inicializarControles(self, datos):
        """
        Inicializa los controles de acuerdo a un diccionario
        """
        for elem in datos.items():
            self.widgets[elem[0]].set_color(datos[elem[0]]) 
       
    def getMapaActual(self, formato="rgb"):
        """
        Regresa el mapa de colores actual en un diccionario
        El metodo get_default_style no regresa el mapa de colores actual
        si esta customizado sino el que corresponde al tema por defecto de gnome (Default) 
        """
        #Busco un widget al azar por ejemplo la ventana
        ventana = self.widgets["principal"]
        
        datos={}
        datos["FG_NORMAL"]=gtk.Widget.get_style(ventana).fg[0]
        datos["FG_PRELIGHT"]=gtk.Widget.get_style(ventana).fg[1]
        datos["FG_ACTIVE"]=gtk.Widget.get_style(ventana).fg[2]
        datos["FG_SELECTED"]=gtk.Widget.get_style(ventana).fg[3]
        datos["FG_INSENSITIVE"]=gtk.Widget.get_style(ventana).fg[4]
        
        datos["BG_NORMAL"]=gtk.Widget.get_style(ventana).bg[0]
        datos["BG_PRELIGHT"]=gtk.Widget.get_style(ventana).bg[1]
        datos["BG_ACTIVE"]=gtk.Widget.get_style(ventana).bg[2]
        datos["BG_SELECTED"]=gtk.Widget.get_style(ventana).bg[3]
        datos["BG_INSENSITIVE"]=gtk.Widget.get_style(ventana).bg[4]
        
        datos["BASE_NORMAL"]=gtk.Widget.get_style(ventana).base[0]
        datos["BASE_PRELIGHT"]=gtk.Widget.get_style(ventana).base[1]
        datos["BASE_ACTIVE"]=gtk.Widget.get_style(ventana).base[2]
        datos["BASE_SELECTED"]=gtk.Widget.get_style(ventana).base[3]
        datos["BASE_INSENSITIVE"]=gtk.Widget.get_style(ventana).base[4]

        datos["TEXT_NORMAL"]=gtk.Widget.get_style(ventana).text[0]
        datos["TEXT_PRELIGHT"]=gtk.Widget.get_style(ventana).text[1]
        datos["TEXT_ACTIVE"]=gtk.Widget.get_style(ventana).text[2]
        datos["TEXT_SELECTED"]=gtk.Widget.get_style(ventana).text[3]
        datos["TEXT_INSENSITIVE"]=gtk.Widget.get_style(ventana).text[4]


        if formato=="rgb":
            #    datos["FG_INSENSITIVE"]=self.getHexString(gtk.widget_get_default_style().fg[0])
            #    datos["FG_NORMAL"]=self.getHexString(gtk.widget_get_default_style().fg[1])
            #    datos["FG_SELECTED"]=self.getHexString(gtk.widget_get_default_style().fg[2])
            #    datos["FG_ACTIVE"]=self.getHexString(gtk.widget_get_default_style().fg[3])
            #datos["FG_PRELIGHT"]=self.getHexString(gtk.widget_get_default_style().fg[4])
            pass 
        return datos 

    #----------------------------------------------------------------------

    def on_btn_cancelar_clicked(self, *args):
        winage = self.widgets['principal']
        winage.destroy()
        gtk.main_quit()
        pass

    #----------------------------------------------------------------------

    def on_btn_aplicar_clicked(self, *args):
        """
        Se ocupa de grabar los datos de los colores y los aplica de inmediato
        """
        #Llamo al metodo que graba los datos
        self.grabarDatos()
        #Los aplico instantaneamente
        self.recargarTema()

    #---------------------------------------------------------------------
    
    def recargarTema(self):
        """
        Recarga el tema GTK
        """
        #Aca recargo el tema gtk pero de una manera sucia, o sea llamando a gconftool, deberia usar una señal.
        #Primero debo capturar el nombre del estilo actual para restablecerlo despues
        #estilo = "Clearlooks" #get...
        os.system("./refresca.sh")

    def getHexString(self, gcolor):
        """
        Arma la representacion Hexadecimal correspondiente para un elemento gdkColor
        """
        return "#" + self.gdkColorToHex(gcolor.red)+ self.gdkColorToHex(gcolor.green) + self.gdkColorToHex(gcolor.blue)

    def gdkColorToHex(self, gcolor):
        """
        Devuelve un numero hexadecimal de dos cifras para un color gdk completo
        """
        return  string.zfill(hex(gcolor).__str__()[2:4],2) 

    def grabarDatos(self):
        """
        Se ocupa de grabar los datos en el archivo correspondiente
        """    
        datos = {}
        #Ahora debo capturar el contenido de los widgets de seleccion de color
        #Voy a empezar probando con uno y veo si despues se puede hacer un for con el nombre del control
        #Y tambien quiero ver si puedo crear array de controles
        
        #Inicializo datos (de una manera poco elegante)
        datos["FG_NORMAL"] = "" 
        datos["FG_ACTIVE"]= ""
        datos["FG_PRELIGHT"]= ""
        datos["FG_SELECTED"]= ""
        datos["FG_INSENSITIVE"]= ""
        datos["BG_NORMAL"] = ""
        datos["BG_ACTIVE"] = ""
        datos["BG_PRELIGHT"]= ""
        datos["BG_SELECTED"]= ""
        datos["BG_INSENSITIVE"]= ""
        datos["BASE_NORMAL"]= ""
        datos["BASE_ACTIVE"]= ""
        datos["BASE_PRELIGHT"]= ""
        datos["BASE_SELECTED"]= ""
        datos["BASE_INSENSITIVE"]= ""
        datos["TEXT_NORMAL"]= ""
        datos["TEXT_ACTIVE"]= ""
        datos["TEXT_PRELIGHT"]= ""
        datos["TEXT_SELECTED"]= ""
        datos["TEXT_INSENSITIVE"]= ""
        
        for elem in datos.items():
            color = self.widgets[elem[0]].get_color()
            datos[elem[0]] = self.getHexString(color)

        #Llamo a gtkRc y le paso un diccionario con los colores
        comp = cambiarcolores.gtkRcCompose(datos)
        comp.createGtkRc()

    def on_btn_resetear_clicked(self, *args):
        """   
        Vuelve los colores a lo guardado
        """
        datos=self.getMapaActual()
        self.inicializarControles(datos)

    


#----------------------------------------------------------------------

def main(argv):

    w = gcolor()
    w.show()
    gtk.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
