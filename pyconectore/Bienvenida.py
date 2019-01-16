import kivy
from kivy.uix.boxlayout import BoxLayout
import main_
#import graficas


kivy.require('1.10.1')
#import matplotlib
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.app import App
from kivy.lang import Builder
import matplotlib.pyplot as plt
#matplotlib.use('PS')
import numpy as np
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.config import Config
from dateutil import parser

Builder.load_string('''

<inicio_>
    BoxLayout:
        orientation: "vertical" 
        padding: 40, 40, 40, 40
        canvas:
            Color:
                rgba: 1, 1, 1, .8
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text:"MEDIDOR DE CONSUMO DE ENERGÍA PORTÁTIL "
            bold: True
            font_size: 21
            multiline: True
            color: [.4,.4,.4,1]
            size_hint_y: .8
            
        Label:
            #multiline: True
            text:" Si ya se cuenta con un equipo registrado pulse -Siguiente-"
            font_size: 18
            multiline: True
            color: [.4,.4,.4,1]
            size_hint_y: .5
        Label:
            text:"De lo contrario pulse -registrar – "
            font_size: 18
            multiline: True
            color: [.4,.4,.4,1]
            size_hint_y: .5
        Label:
            text:"Recuerde que necesita previamente un registro en el servidor"
            font_size: 18
            multiline: True
            color: [.4,.4,.4,1]
            size_hint_y: .5
        BoxLayout:
            orientation: "horizontal"
            spacing:80
            padding:50
            Button:
                text:"Registrar"
                id: but_1
                size_hint: .5, 1
                on_press:root.manager.current = 'Bienvenida'
            Button:
                text:"Siguiente"
                id: but_2
                size_hint: .5, 1
                on_release:root.manager.current= 'Enable'
<bienvenida>
    BoxLayout:
        orientation: "horizontal"
        canvas:
            Color:
                rgba: 1, 1, 1, .8
            
            Rectangle:
                size: self.size
                pos: self.pos 
                
        BoxLayout:
            Image:
                size_hint:.5,1
                source:'science2.jpg'
                allow_stretch: True
            BoxLayout:
                cols:2
                orientation: 'horizontal' 
                padding: 20,20,20,20
                spacing: 30
                BoxLayout:
                    orientation:'vertical'
                    Image: 
                        source: 'log.png' 
                        size_hint_x: .4
                        size_hint_y: .7
                    Label: 
                        text: "MEDIDOR DE CONSUMO DE ENERGÍA PORTÁTIL."
                        bold: True
                        font_size: 21
                        multiline: True
                        color: [0,0,0,1]
                        size_hint_y: .8
                    Label:
                        text:"El asistente de instalacion lo guiara para el registro del servidor " 
                        font_size:17
                        color: [0,0,0,1]
                        size_hint_y: .5
                    Label:
                        text:"Esta herramienta registrara el cliente en el servidor, Estara ejecutandose como un servicio de lectura constante y trasmición de datos. da click en siguiente para continuar, o Cancelar para Salir.      "
                        color: [0,0,0,1]
                        italic: True
                        multiline:True
                        text_size: self.size
           
                    BoxLayout:    
                        padding: 10
                        spacing: 20
                        Button:
                            text: "Cancelar "
                            size_hint: .5, .35
                            on_press:app.stop()
                        Button:
                            text:"Siguiente"
                            size_hint: .5, .35
                            on_press:root.manager.current = 'Acuerdo de licencia'
<acuerdo>
    BoxLayout:
        orientation: "horizontal"
        canvas:
            Color:
                rgba: 1, 1, 1, .8
            Rectangle:
                size: self.size
                pos: self.pos 
        BoxLayout:
            Image:
                size_hint:.5,1
                source:'science2.jpg'
                allow_stretch: True
            BoxLayout:
                cols:2
                orientation: 'horizontal' 
                padding: 20, 20, 20, 20
                Image: 
                    source: 'log.png' 
                    size_hint_x: .2
                    size_hint_y: 1.8
                BoxLayout:
                    orientation:'vertical'
                    Label: 
                        text: "Acuerdo de licencia y uso del Software ."
                        bold: True
                        font_size: 21
                        multiline: True
                        color: [0,0,0,1]
                        size_hint_y: .8
                    Label:
                        text:"Favor de leer los siguientes acuerdos de licencia antes de continuar. " 
                        font_size:17
                        color: [0,0,0,1]
                        size_hint_y: .5
                        multiline:True
                        text_size: self.size
                    TextInput:
                        text:" En este apartado van los acuerdos de licencia del software a presentar, los cuales ase an omitido por el momento.  "
                        size_hint: 1, 2
                        readonly:True
                        
                    Label:
                        text:"Debes de aceptar los terminos de licencia para poder continuar. " 
                        font_size:14
                        color: [0,0,0,1]
                        size_hint_y: .4
                        multiline:True
                        text_size: self.size
                    GridLayout:
                        cols:2
                        spacing: '18dp'
                        size_hint: .5, None
                        height: self.minimum_height
                        #spacing:10
                        CheckBox:
                            id:noacept
                            size_hint_y: None
                            height: '20dp'
                            group: '1a'
                            color: [0,0,0,1]
                            active: False
                        Label:
                            text:'Aceptar licencia'
                            color: [0,0,0,1]
                        CheckBox:
                            size_hint_y: None
                            height: '20dp'
                            group: '1a'
                            color: [0,0,0,1]
                            #on_press:root.manager.current = 'quit'
                        Label:
                            text: 'No aceptar licencia' 
                            color: [0,0,0,1]
                    BoxLayout:
                        orientation:'horizontal'
                        Button:
                            text:"regresar"
                            size_hint: .5, .4
                            on_press:root.manager.current = 'Bienvenida'
                        Button:
                            text:"Siguiente"
                            size_hint: .5, .4
                            on_press:root.manager.current = 'Conexión'
                            disabled: not noacept.active 

<conexion>
    BoxLayout:
        orientation: "horizontal"
        canvas:
            Color:
                rgba: 1, 1, 1, .8
            Rectangle:
                size: self.size
                pos: self.pos 
        BoxLayout:

            #size_hint:1,1
            Image:
                size_hint:.5,1
                source:'science2.jpg'
                #center_y: 40
                #size: 250, 200
                allow_stretch: True

            BoxLayout:
                cols:2
                orientation: 'horizontal' 
                padding: 20, 20, 20, 20
                spacing:10
                Image: 
                    source: 'log.png' 
                    #size: 120,120
                    size_hint_x: .2
                    #width: 5
                    size_hint_y:1.9
                BoxLayout:
                    orientation:'vertical'
                    Label: 
                        text: "   Conexion con servidor "
                        bold: True
                        font_size: 21
                        multiline: True
                        color: [0,0,0,1]
                        size_hint_y: .6
                    Label:
                        text:"Ingrese los siguientes datos:"                        
                        font_size:17
                        color: [0,0,0,1]
                        size_hint_y: .3
                        multiline:True
                        #text_size: self.size
                    GridLayout:
                        cols:2
                        spacing: '15dp'
                        #padding: 15
                        size_hint: 1, 2.5
                        #height: self.minimum_height
                        Label:
                            text:"HOST"
                            color:[0,0,0,1]
                            spacing: '20dp'
                        TextInput:  
                            size_hint:1, 1
                            id:host
                        Label:
                            text:"PUERTO MODBUS"
                            color:[0,0,0,1]
                        TextInput:  
                            size_hint:1, 1
                            id:modbus
                        Label:
                            text:"DNS"
                            color:[0,0,0,1]
                            spacing: '20dp'
                        TextInput:  
                            size_hint:1, 1
                            id:dns
                        Label:
                            text:"CANAL"
                            color:[0,0,0,1]
                        TextInput:  
                            size_hint:1, 1
                            id:canal
                        Label:
                            text:"PUERTO SERVIDOR"
                            color:[0,0,0,1]
                        TextInput:  
                            size_hint:1, 1
                            #text:" puerto de trasmicion"
                            id:puerto
                        Label:
                            text:"ID DE CLIENTE"
                            color:[0,0,0,1]
                        TextInput:   
                            size_hint:1, 1
                            id:cliente
                        Label:
                            text:"USUARIO"
                            color:[0,0,0,1]
                        TextInput:  
                            size_hint:1, 1
                            #text: "pidelo al servidor "
                            id:usuario
                        Label:
                            text:"PASSWORD"
                            color:[0,0,0,1]
                        TextInput:  
                            size_hint:1, 1
                            #text:"pidelo al servidor"
                            id:password  
                    BoxLayout:
                        orientacion:'vertical'
                        spacing:10
                        Button:
                            id:btn1
                            text:"Probar conexión"
                            size_hint: .5, .4
                            on_release:root.build1()
                        Button:
                            text:"regresar"
                            size_hint: .5, .4
                            on_press:root.manager.current = 'Acuerdo de licencia'
                        Button:
                            text:"Guardar"
                            id:Guarda
                            size_hint: .5, .4
                            on_release:root.manager.current= 'Enable'
                            on_press:root.next_main()
                            
<enableconex>
    BoxLayout:

        orientation: "vertical"
        padding: 40, 40, 40, 40
        spacing:10
        #Title: "Graficas"
        canvas:
            Color:
                rgba: 0, 0, 0, .5
            Rectangle:
              
        Label:
            text: 'Ventana de graficas '
            bold: True
            font_size: 21
            multiline: True
            color: [.4,.4,.4, 1]
            size_hint_y: .8
            
        BoxLayout:
            orientation: "horizontal"
            Button:
                text: "Tension"
                size_hint: 1, 1
                on_press:root.tensio
            Button:
                text: "Corriente "
                size_hint: 1, 1
                on_press:root.corrien
            Button:
                text: "corrienteMaxima "
                size_hint: 1, 1
                on_press:root.corrienteMaxi
            Button:
                text: "Potencia Aparente"
                size_hint: 1, 1
                on_press:root.potenciaAparen
        BoxLayout:        
            Button:
                text: "Potencias Activas"
                size_hint: 1, 1
                on_press:root.potenciasActiv
            Button:
                text: "Potencias Reactivas"
                size_hint: 1, 1
                on_press:root.potenciaReacti
            Button:
                text: "Factor Potencia "
                size_hint: 1, 1
                on_press:root.factorPotenc
            Button:
                text: "Factor Potencia Minima "
                size_hint: 1, 1
                on_press:root.factorPotenciaMi
                
        Button:
            text: "Salir "
            size_hint: 1, .5
            on_press:app.stop()
''')



class inicio_(Screen):
    pass
class bienvenida(Screen):
    pass
class acuerdo(Screen):
    print("este mensaje es para consola, define el advance del proyecto")
    pass
class conexion(Screen):

    def build1(self):
        self.ids.Guarda.active = False
        if main_.on_conexion():
            main_.host = self.ids.host.text
            main_.modbus = self.ids.modbus.text
            main_.dns = self.ids.dns.text
            main_.canal = self.ids.canal.text
            main_.puerto = self.ids.puerto.text
            main_.id_cliente = self.ids.cliente.text
            main_.usuario = self.ids.usuario.text
            main_.password = self.ids.password.text

            self.ids.Guarda.active = True
        else:
            self.ids.host.text = ''
            self.ids.modbus.text = ''
            self.ids.dns.text = ''
            self.ids.canal.text = ''
            self.ids.puerto.text = ''
            self.ids.cliente.text = ''
            self.ids.usuario.text = ''
            self.ids.password.text = ''
            self.ids.Guarda.active = False


    print("valores recibidos:",main_.dns, ",", main_.canal, ",", main_.puerto, ",", main_.id_cliente, ",", main_.usuario, ",", main_.password)
    def next_main(self):
        print("regreso a main")
        main_.bienv()

class enableconex(Screen):
    #import conexion_hivemq

    def tensio(self):
        #main_.mqtt_
        datat = main_.grafico
        dates = []
        values = []
        for row in datat:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Tencion')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        plt.show()
        Clock.shedu
        return box

    def corrien(self):
        datacor = main_.grafico
        dates = []
        values = []
        for row in datacor:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Corriente')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box
    def corrienteMaxi(self):
        datacorMax = main_.grafico
        dates = []
        values = []
        for row in datacorMax:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Corriente MAxima')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box
    def potenciasActiv(self):
        datapotact = main_.grafico
        dates = []
        values = []
        for row in datapotact:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Potencia Activa')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box
    def potenciaReacti(self):
        datapotrea = main_.grafico
        dates = []
        values = []
        for row in datapotrea:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Potencia Reactiva')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box
    def potenciaAparen(self):
        datapotapa = main_.grafico
        dates = []
        values = []
        for row in datapotapa:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Potencia Aparente')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        plt.show()
        return box
    def factorPotenc(self):
        datafacpot = main_.grafico
        dates = []
        values = []
        for row in datafacpot:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Factor Potencia')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box
    def factorPotenciaMi(self):
        datafacpotm = main_.grafico
        dates = []
        values = []
        for row in datafacpotm:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        plt.plot_date(dates, values, 'x-')
        plt.ylabel('Factor Potencia Minima')
        plt.xlabel('Tiempo')
        box = BoxLayout()
        return box

class acuerdoApp(App):
    def build(self):
        return sm

sm = ScreenManager()
sm.add_widget(inicio_(name='iniciando'))
sm.add_widget(bienvenida(name='Bienvenida'))
sm.add_widget(acuerdo(name='Acuerdo de licencia'))
sm.add_widget(conexion(name='Conexión'))
sm.add_widget(enableconex(name='Enable'))

acuerdoApp().run()