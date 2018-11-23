#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cuenta import*
class Cliente:

  def __init__(self,nomb,dire,edad):
  
    self.__nombre=nomb

    self.__direccion=dire
  
    self.__edad=edad
  
    self.cuentas=[]

#nuevo métodos para que el cliente pueda tener más de una cuenta

  def AñadirCuenta(self,cuenta):
    self.__cuentas.append(cuenta)
    print("El cliente "+self.__nombre+" agrego una nueva cuenta")

#Método para poder eliminar una cuenta de la lista de cuentas 

  def EliminarCuenta(self,cuenta):

    if cuenta in self.cuentas:  
        self.cuentas.remove(cuenta)
        print("El cliente "+self.__nombre+" ha eliminado una cuenta")
    else:
        print("La cuenta no existe")

  def getCuenta (self,cuenta):
    return self.cuentas[index]

  def infoCuentas( self ):
        for cuenta in self.cuentas:
            print ( cuenta )

  def getDireccion(self):
      return self.__direccion 
    
    #para poder ver que nuestra funcion set ha cambiado la direccióón
  
    
  def setDireccion(self,nuevadir):
  
      self.__direccion=nuevadir
    #aquí se implementó el set porque la dirección de un cliente puede modificarse en cualquier momento, sin embargo en los otros datos no es necesario porque son datos que no cambian-

   
  def __str__(self):
    
    temp="Nombre: "+str(self.__nombre)
    temp+="\n Direccion: "+str(self.__direccion)
    temp+="\n Edad: "+str(self.__edad)

    return temp