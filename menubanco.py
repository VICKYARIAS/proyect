#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cliente import*
import sys
from CuentaDeAhorro import *
from CuentaDeCredito import*
from Banco import *
from Menu import*
from MenuCuentaBasica import*
from Menu_Usuario import*

class MenuBanco:
  def __init__(self):
    self.opciones={

      "1": self.AgregarunCliente,
      "2": self.EliminarunCliente,
      "3": self.salir
    }

  def MostrarMenu(self):
    print (""" 
    
    Este es el menú del banco:
    1 Agregar un Cliente
    2 Eliminar un Cliente
    3 Salir""")
  #Éste método muestra el menú y responde a las elecciones

  def Correr(self):
    
    while True:
      self.MostrarMenu()

      opcion= input("\nEliga una opciòn:")

      accion= self.opciones.get(opcion)

      if accion:
         accion()
      else:
        print("\n{0} no es una opción válida" "\n\nElija otro opción".format(opcion))
  
  def AgregarunCliente(self):

      print("Eligió agregar un CLiente: \n"+"\n\n Llene los siguientes datos:"+ "\n")
      nombre=input("Nombre del cliente: ")
      edad=str(input("Edad: "))
      direccion=input("Dirección: ")
      print("Datos del cliente: \n")
      cliente=Cliente(nombre,direccion,edad)
      
      print(cliente)

      
  def EliminarunCliente(self):
      print("Eligió eliminar un CLiente: \n"+"\n\n Llene los siguientes datos:"+ "\n")
      cliente= input("\n¿Cuál es el cliente que desea eliminar?")
      self.Banco.EliminarCliente(cliente)


  def salir(self):
    print("\n\n\t***Gracias por su preferencia, hasta luego.***")
    sys.exit(0)

    #No pude utilizar el método EliminarCLiente porque decía que Banco no era un atributo de la clase menu banco
