#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cliente import*
class  Banco:
  def __init__(self,nom,ubic):

    self.__nombre=nom
    
    self.__ubicacion=ubic
    
    self.__clientes=[]
  
  #nuevo métodos para que el banco pueda tener más de un cliente

  def AñadirCliente(self,cliente):
    self.__clientes.append(cliente)
    print("Se ha agregado un nuevo cliente ")

  #Método para poder eliminar un cliente de la lista de clientes

  def EliminarCliente(self,cliente):

    if cliente in self.__clientes:  
        self.__clienes.remove(cliente)
        print("Se ha eliminado una cuenta")
    else:
        print("La cuenta no existe")

  def getCliente (self,cliente):
    return self.__Clientes[index]

  def infoClientes( self ):
        for cta in self.cuentas:
            print ( cta )

  def __str__(self):
  
    cadena=" El nombre del Banco es:" +str(self.__nombre)
    cadena+="\n Su Ubicación es: "+str(self.__ubicacion)
    cadena+="\n Cliente: "+str(self.__cliente)
    return cadena