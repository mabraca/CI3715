import unittest
import Tarifa
from datetime import datetime, timedelta
from unittest.case import TestCase

class TestTarifa(unittest.TestCase):
    def test_1(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n El mismo dia, y solo 25 minutos en dia de Semana")
        mas_25min = datetime(2017, 10, 5, 18, 39)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_25min)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),100)
    
    def test_2(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n El mismo dia, y solo 25 minutos en fin de Semana")
        ahora2 = datetime(2017, 10, 7, 18, 14)
        mas_25min = datetime(2017, 10, 7, 18, 39)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora2, mas_25min)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),200)
    
    def test_3(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n El mismo dia y mas dos horas en dia de Semana")
        mas_2hrs = datetime(2017, 10, 5, 21, 14)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_2hrs)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),400)
        
    def test_4(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 4, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n Dos dias despues y dos horas despues en dia de semanas")
        mas_2hrsfin = datetime(2017, 10, 6, 20, 14)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_2hrsfin)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),5100)
        
    def test_5(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n Empieza en dia de semana y termina un Sabado")
        dFinDeSemana = datetime(2017, 10, 7, 18, 14) 
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, dFinDeSemana)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),6800)
        
    def test_6(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n Empieza en dia de semana y termina un Domingo")
        dDomingo = datetime(2017, 10, 8, 18, 14) 
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, dDomingo)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),11600)
        
    def test_7(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n Empieza un dia despues de que termina")
        dDespues = datetime(2014, 10, 4, 18, 14)
        self.assertRaises(ValueError, calcular.tiempoDeTrabajo, ahora, dDespues)
    
    def test_8(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("\n Maximo de dias superado") 
        mas7d = datetime(2017, 10, 13, 18, 14) 
        self.assertRaises(ValueError, calcular.tiempoDeTrabajo, ahora, mas7d)
        
    def test_9(self):
        
        calcular = Tarifa.Calculo()
        ahora = datetime(2017, 10, 5, 18, 14)
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        
        print("Tiempo menor") 
        mas14m = datetime(2017, 10, 5, 18, 14)
        self.assertRaises(ValueError, calcular.tiempoDeTrabajo, ahora, mas14m)
        
        
if __name__ == '__main__':
    unittest.main()