pruebas
print ( " \ n \ n \ t ********* Objeto Cliente: sin cuentas " )
cliente1 = Cliente ( " Alejandro " , " Calle Flores No.25 " , 56 )
print( str (cliente1))
cliente1.infoCuentas ()

cuenta1=CuentaDeCredito(8000,500,"16%", "Cuenta de Crédito")

cuenta2 = CuentaDeAhorro(5000,"16%" , "Cuenta de Ahorro")

cuenta3=CuentaDeCredito(7000,1500,"16%", "Cuenta de crédito")

print ( " \n\t\t**Pruebas del método añadir cuentas**\n\n" )
cliente1.AñadirCuenta (cuenta1)
cliente1.AñadirCuenta (cuenta2)
cliente1.AñadirCuenta (cuenta3)
cliente1.infoCuentas ()
print ( " \n\t\t**Pruebas del método eliminar cuentas**\n\n" )
cliente1.EliminarCuenta (cuenta1)
cliente1.infoCuentas ()

cliente2 = Cliente("Victoria", "Guanajuato", 25)
cliente2.AñadirCuenta(cuenta3)

banco1= Banco("Banamex","ubicación")
print (banco1)
print(" \n\t\t**Pruebas del método añadir clientes**\n\n")
banco1.AñadirCliente(cliente1)
banco1.AñadirCliente(cliente2)
banco1.infoCliente()