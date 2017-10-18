import unittest
from BilleteraElectronica import BilleteraElectronica

class Test_Billetera(unittest.TestCase):  
    
    def test_0(self):
        """ Recargo y consumo el mismo monto"""
        print("Recargo y consumo el mismo monto")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(100, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(),0)
    
    def test_01(self):
        """ Recargo mas de lo que consumo"""
        print("Recargo mas de lo que consumo")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(50, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(),50)
    
    def test_1(self):
        """ Consumo mas de lo que recargue"""
        print("Consumir mas de lo que recargue en la cuenta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(250, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(), 100)
    
    def test_2(self):
        """ Consumir con clave incorrecta"""
        print("Consumir con clave incorrecta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(50, "22/15/2017", "Comercio1", 20267824, 123)
        self.assertEqual(billetera1.saldo(), 100)
     
    def test_3(self):
        """ Consumir con cedula incorrecta"""
        print("Consumir con cedula incorrecta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(50, "22/15/2017", "Comercio1", 20267823, 1234)
        self.assertEqual(billetera1.saldo(), 100)
    
    def test_4(self):
        """ Consumir con cedula y clave incorrecta"""
        print("Consumir con clave y cedula incorrecta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(50, "22/15/2017", "Comercio1", 20267823, 1235)
        self.assertEqual(billetera1.saldo(), 100)
    
    def test_41(self):
        """ Consumir con clave correcta y cedula correcta"""
        print("Consumir con clave correcta y cedula correcta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(50, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(), 50)

    def test_5(self):
        """ Recargar saldo negativo"""
        print("Recargar saldo negativo")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(-100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(),0)
        
    def test_6(self):
        """ Recargar con cedula incorrecta"""
        print("Recargar con cedula incorrecta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267823)
        self.assertEqual(billetera1.saldo(), 0)
    
    def test_61(self):
        """ Recargar con cedula correcta"""
        print("Recargar con cedula correcta")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
    
    def test_7(self):
        """ Consumir cantidad negativa"""
        print("Consumir cantidad negativa")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(-50, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(), 100)
    
    def test_8(self):
        """ Recargar 0"""
        print("Recargar 0 bs")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(0, "20/12/2017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 0)
    
    def test_9(self):
        """ Consumir 0 sin haber recargado"""
        print("Consumir 0 bs sinb haber recargado")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.consumir(0, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(), 0)
     
    def test_10(self):
        """ Consumir 0 y haber recargado"""
        print("Consumir 0 bs y haber recargado")
        billetera1=BilleteraElectronica(1,"Maria", "Bra", 20267824, 1234)
        billetera1.recargar(100, "20/12/2sinb017", "Comercio1", 20267824)
        self.assertEqual(billetera1.saldo(), 100)
        billetera1.consumir(0, "22/15/2017", "Comercio1", 20267824, 1234)
        self.assertEqual(billetera1.saldo(), 100)
        
        
if __name__ == '__main__':
    unittest.main()