'''
Created on 08/10/2017

@author: Maria Bracamonte y Luis Serrano
'''

            
class BilleteraElectronica:
    """Datos personales del dueño PIN(Personal Identification Number) es un código secreto a la hora de autentificar la
    identidad del usuario"""
    def __init__(self, ident, nombres, apellidos, CI, PIN):
        self.id=ident
        self.saldoPrincipal=0
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.PIN=PIN

    #Estructura de Credito
    class Credito:
        """Registra recargas relacionados a la billetera electrónica"""
        def __init__(self, monto, fecha, ident):
            self.monto=monto
            self.fecha= fecha
            self.id= ident
        def __repr__(self):
            """Para imprimir en pantalla """
            return "Linea de credito \n [ %f,%s,%s]" % (self.monto, self.fecha, self.id)
          
    #Estructura de Dedito    
    class Debito:
        """Registra los débitos (consumos) relacionados a la billetera electrónica"""
        def __init__(self, monto, fecha, ident):
            self.monto=monto
            self.fecha= fecha
            self.id= ident
            
        def __repr__(self):
            """Para imprimir en pantalla """
            return "Linea de debito \n Monto: %d,Fecha: %s, ID Neg %i" % (self.monto, self.fecha, self.id)
      
      
    def saldo(self):
        print(self.saldoPrincipal)
        return self.saldoPrincipal
    
    def recargar(self, monto, fecha, ident, CI):
        if CI== self.CI:
            if monto>0:
                self.Credito(monto, fecha, ident)
                self.saldoPrincipal= self.saldoPrincipal + monto
                return True
            else:
                print("No puede recargar saldo negativo")
                return False
        else:
            print("ERROR. Usuario incorrecto")
            return False
    
    def consumir(self, monto, fecha, ident, CI, PIN):
        if CI==self.CI and PIN==self.PIN:
            if monto<0:
                print("Error. Monto de consumo negativo")
                return False
            if self.saldoPrincipal>=monto:
                self.Debito(monto, fecha, ident)
                self.saldoPrincipal= self.saldoPrincipal - monto
                return True
            else:
                print("ERROR. Saldo insuficiente")
                return False
        else:
            print("ERROR. El consumo no esta permitido. Dato incorrecto")
            return False
        
