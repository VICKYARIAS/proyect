import sys
from Banco import Cliente
import os
from Cliente import*
from CuentaDeAhorro import *
from CuentaDeCredito import*
from Banco import *

class Menu:

  def __init__ (self,nombre,ubicacion):

    Banco.__init__(self,nombre,ubicacion)

    self.cliente=None
    self.clientes=[]

    self.Bienvenida= "\n******* Bienvenido ***********\n"

    self.opciones={

      "1": self.CrearunCliente,
      "2": self.IngresaraunCliente,
      "3": self.salir
    }

    self.opciones2={

      "1": self.AgregarunaCuenta,
      "2": self.retirar,
      "3": self.depositar,
      "4": self.salir
    }

  def MenuPrincipal(self):
    print("\n\n\t~~~~~~~~~Banco Patito~~~~~~~~")
    print("\n\n *Bienvenido* ","\n")
    print("Elija la opción adecuado a lo que desa: ","\n")
    opcion=input("1.-Ingresar al Menu del Banco"+"\n2.-Ingresar al Menu de la Cuenta "+"\n3.-Salir"+"\n")
    while opcion!="1" and opcion!="2" and opcion!="3":
          opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
    if opcion=="1":
        self.CorrerBanco()
    if opcion=="2":
        self.CorrerCuenta()
    if opcion=="3":
        print("\n\t**Gracias por su preferencia, hasta luego.**")
        sys.exit(0)   
  def MostrarMenuBanco(self):
    print (""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Menú del banco:
    1 Crear un Cliente
    2 Ingresar a la iformación de un Cliente
    3 Salir""")
  #Éste método muestra el menú y responde a las elecciones

  def CorrerBanco(self):
    
    while True:
      self.MostrarMenuBanco()

      opcion= input("\nEliga una opciòn:")

      accion= self.opciones.get(opcion)

      if accion:
         accion()
      
      else:
        print("\n{0} no es una opción válida" "\n\nElija otro opción".format(opcion))

     
  
  def CrearunCliente(self):

      print("Eligió agregar un CLiente: \n"+"\n\n Llene los siguientes datos:"+ "\n")
      nombre=input("Nombre del cliente: ")
      edad=str(input("Edad: "))
      direccion=input("Dirección: ")
      print("****Datos del cliente: \n*****")
      self.cliente=Cliente(nombre,direccion,edad)
      self.clientes.append(self.cliente)
      print(self.cliente)
      Banco.AñadirCliente(self.cliente)
      
      print("\n\nElija la opción que corresponda a lo que desea hacer")
      

      print("""
      1. Ingresar al Menu del Banco
      2. Ingresar al Menu de la Cuenta
      3. Salir
      """)

      opcion=input()
      while opcion!="1" and opcion!="2" and opcion!="3":
          opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
      if opcion== "1":
        self.MenuPrincipal()
      if opcion=="2":
        self.CorrerBanco()
      if opcion=="3":
        print("\n\t**Gracias por su preferencia, hasta luego.**")
        sys.exit(0) 
      
  def IngresaraunCliente(self):
      if len(self.clientes)!=0:
            print("Clientes registrados en el banco: ","\n")
            temp=""
            for i in range(len(self.clientes)):
              temp="Cliente "+str(i+1)+"\n\n"
              temp+="Nombre del cliente: "+self.clientes[i].nombre+"\n"
              cadena+="Número de cuentas: "+str(len(self.clientes[i].cuenta))+"\n"
              print(cadena)  
            
            ver_cliente=input("Indique que número de cliente es al que quiere ingresar"+" o presione 'x' para volver al menú del banco\n")
            for i in range(len(self.clientes)):                
              if int(ver_cliente)==i+1:
                  men=""
                  print("\nCuentas del cliente "+"\n")
                  for j in range(len(self.clientes[i].cuenta)):
                      men="Cuenta "+str(j+1)+"\n"+str(self.clientes[i].cuenta[j])
                      print(c)
            if ver_cliente.lower()=="x":
                self.CorrerBanco()
                  
      else:
            print("No hay clientes registrados en el Banco Patito")
            self.CorrerBanco()


  def salir(self):
    print("\n\n\t***Gracias por su preferencia, hasta luego.***")
    sys.exit(0)
    
  def MostrarMenuCuenta(self):
    print (""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Menú de la Cuenta
    1 Crear una cuenta
    2 Retirar
    3 Depositar
    4 Salir""")
  #Éste método muestra el menú y responde a las elecciones
  def CorrerCuenta(self):
    
    while True:
      self.MostrarMenuCuenta()

      opcion= input("\nEliga una opciòn:")

      accion= self.opciones2.get(opcion)

      if accion:
         accion()
      else:
        print("\n{0} no es una opción válida" "\n\nElija otro opción".format(opcion))
    
  
  def retirar(self):

    cantidad= input("¿Qué cantidad desea reitrar?")
    self.Cuenta.retirar(int(cantidad))

  def depositar(self):

    cantidad= input("\n¿Qué cantidad desea depositar?")
    self.Cuenta.depositar(int(cantidad))

  def AgregarunaCuenta(self):
  
    msg="\nEligió agregar una cuenta "
    msg+="\n\nTipos de cuenta"
    msg+="\n1. Cuenta de Ahorro"
    msg+="\n2.Cuenta de Crédito"
    print(msg)
    tipo=input("\nElija el tipo de cuenta:")
    cuentas=[]
    if int(tipo)==1:
      print("\nPara crear la Cuenta de Ahorro inserte los siguientes datos: "+ "\n" )
      SaldoInicial=int(input("\nSaldo inicial: $ " ))
      TasadeInteres=int(input("Tasa de interés:"))
      Tipo="Cuenta de Ahorro"

      print("\nCUENTA REGISTRADA\n")
     
      print("Datos de la cuenta: \n ")

      cuenta=CuentaDeAhorro(SaldoInicial,TasadeInteres,Tipo)

      Cliente.AñadirCuenta(cuenta)
      

      print(cuenta)

      print("\n\n¿Elija la opción que corresponda a lo que desea hacer?")
      

      print("""
      1. Ingresar al Menu del Banco
      2. Ingresar al Menu de la Cuenta
      3. Salir
      """)

      opcion=input()
      while opcion!="1" and opcion!="2" and opcion!="3":
          opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
      if opcion== "1":
        self.MenuPrincipal()
      if opcion=="2":
        self.CorrerBanco()
      if opcion=="3":
        print("\n\t**Gracias por su preferencia, hasta luego.**")
        sys.exit(0) 

    if int(tipo)==2:
      print("\nPara crear la Cuenta de Crédito inserte los siguientes datos: "+ "\n" )
      SaldoInicial=int(input("\nSaldo inicial: $ " ))
      TasadeInteres=int(input("Tasa de interés:"))
      Sobregiro=int(input("Sobregiro: $ "))
      Tipo="Cuenta de Crédito"
      cuenta=CuentaDeCredito(SaldoInicial, Sobregiro,TasadeInteres,Tipo)

      print("\nCUENTA REGISTRADA\n")
      print("Datos de la cuenta: \n ")
      print(cuenta)
    if int(tipo)!=2 or int(tipo)!=1:
      print("Opción inválida, vuelva a elegiir")
      
   
    