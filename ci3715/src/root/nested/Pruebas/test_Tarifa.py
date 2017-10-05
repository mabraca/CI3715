import unittest
import Tarifa
from datetime import datetime, time, timedelta
from unittest.case import TestCase

class TestTarifa(unittest.TestCase):
    def test_1(self):
        calcular = Tarifa.Calculo()
        ahora = datetime.now() 
        tarifa = Tarifa.Tarifa()
        tarifa.DiaSemana=100
        tarifa.DiaFinDeSemana=200
        print(" El mismo dia, y solo 25minutos en dia de Semana")
        mas_min = ahora + timedelta(minutes=25)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_min)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),100)
        print(" El mismo dia, y solo 25minutos en Fin de Semana")
        ahora2= ahora + timedelta(days=3)
        mas_min = ahora + timedelta(minutes=25) + timedelta(days=3)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora2, mas_min)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),200)
        print("\n El mismo dia, y mas dos horas en dia de Semana")
        mas_2hrs = ahora + timedelta(hours=2)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_2hrs)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),300)
        print("\n dos dias despues y dos horas despues en dia de semanas")
        mas_2hrsfin = ahora + timedelta(days=2) +timedelta(hours=2)
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_2hrsfin)
        print(tiempo_Servicio)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),9100)
        print("\n Empieza en dia de semana y termina un Sabado")
        mas_3d = ahora + timedelta(days=3) 
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_3d)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),14300)
        print("\n Empieza en dia de semana y termina un Domingo")
        mas_3d = ahora + timedelta(days=3) 
        tiempo_Servicio= calcular.tiempoDeTrabajo(ahora, mas_3d)
        self.assertEqual(calcular.calcularPrecio(tarifa, tiempo_Servicio),14300)
        
if __name__ == '__main__':
    unittest.main()