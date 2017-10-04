from datetime import datetime, time, timedelta
'''
Created on 3/10/2017

@author: Maria Bracamonte 10-11147 Abelardo Salazar 13-11303
'''

class Tarifa:
    pass
class Calculo:
    """Clase Servicio calculara informacion 
    de la inforamcion dada"""
    def __init__(self):
        pass
    
    def tiempoDeTrabajo(self, inicioDeServicio, finDeServicio):
        pagar=[]
        """ Inicio de servicio"""
        dayStart= inicioDeServicio.day
        monthStart= inicioDeServicio.month
        yearStart= inicioDeServicio.year
        hourStart= inicioDeServicio.hour
        minuteStart= inicioDeServicio.minute
        weekDayStart= inicioDeServicio.isoweekday() 
        """Lunes es 1 y Domingo es 7"""
        
        """ Fin de servicio"""
        dayEnd= finDeServicio.day
        monthEnd= finDeServicio.month
        yearEnd= finDeServicio.year
        hourEnd= finDeServicio.hour
        minuteEnd= finDeServicio.minute
        weekDayEnd= finDeServicio.isoweekday() 
      
        """Si el dia inicial es menor que el dia final estando en el mismo mes o la hora final es menor que la hora de entrada estando el mismo dia"""
        if (dayEnd<dayStart and monthEnd==monthStart and yearEnd==yearStart) or (dayEnd==dayStart and monthEnd==monthStart and yearEnd==yearStart and hourEnd<hourStart):
            print("Error en los datos")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """Si el dia de servicio supera mas de siete dias"""
        if dayEnd-dayStart>7 or monthEnd!=monthStart or yearEnd!=yearStart:
            print("El maximo de dias para el servicio ha superado el limite")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """ Ha utilizado menos de 15 minutos del servicio""" 
        if minuteEnd-minuteStart<15 and hourEnd==hourStart and dayEnd==dayStart and monthEnd==monthStart:
            print("Ha tardado menos de 15 minutos, vayase gratis")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """Si el servicio es del mismo dia"""
        if dayEnd==dayStart:
            horaCobrar = hourEnd-hourStart
            if minuteEnd>0:
                horaCobrar += 1
            
            if weekDayStart<6:
                pagar.append(horaCobrar) 
                pagar.append(0)
            else:
                pagar.append(0)
                pagar.append(horaCobrar) 
               
            
            return pagar
            
        else:
            """Si el servicio dura mas de un dia.Tomo los casos de cuando empezo y cuando termino"""
            if weekDayStart<5 and  weekDayEnd<5: 
                """Si el servicio empezo y termino en un dia de semana""" 
                hoursWeekday= (weekDayEnd -1)*24            
                """ Cuantos dias enteros (24hr) se hizo el servicio """
                hoursWeekday= hoursWeekday + (24-hourEnd)   
                """El dia que se termino que no se hizo 24hrs"""
                if minuteEnd>0:
                    hoursWeekday= hoursWeekday + 1          
                    """Si termino con un minuto mas de la hora se le suma otra hora"""
                
                pagar.append(hoursWeekday) 
                pagar.append(0)
                return pagar
            
            elif weekDayStart>5 and  weekDayEnd>5: 
                """Si el servicio empezo y termino en un fin de semana. Empezo sabado y termino domingo"""         
                """ Cuantos dias enteros (24hr) se hizo el servicio """
                hoursWeekday= 24 + (24-hourEnd)   
                """El dia que se termino que no se hizo 24hrs"""
                if minuteEnd>0:
                    hoursWeekday= hoursWeekday + 1          
                    """Si termino con un minuto mas de la hora se le suma otra hora"""
                pagar.append(0)
                pagar.append(hoursWeekday) 
                return pagar
            elif weekDayStart<5 and  weekDayEnd>5: 
                """Si el servicio empezo enn un dia de semana y termino en un fin de semana""" 
                if weekDayEnd==6:
                    hoursWeekday= (weekDayEnd-1)*24 
                    """dias de semana trabajados y termino un sabado"""
                    hoursWeekend= 24-hourEnd
                    if minuteEnd>0:
                        hoursWeekend= hoursWeekend + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
                elif weekDayEnd==7:
                    hoursWeekday= (weekDayEnd-2)*24 
                    """dias de semana trabajados y termino un sabado"""
                    hoursWeekend= (24-hourEnd)+24
                    """dia de fin de semana trabajo uno completo y se le suma la hora del otro fin de semana"""
                    if minuteEnd>0:
                        hoursWeekend= hoursWeekend + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
            elif weekDayStart<5 and  weekDayEnd>5:
                """Si el servicio empezo en un fin de semana y termino en un dia de semana""" 
                if weekDayStart==6:
                    hoursWeekend= (24-hourStart)+24 
                    """Se toma las horas desde que entro y el otro dia de fin de semana completo"""
                    hoursWeekday= (weekDayEnd-1)*24+ (24-hourEnd)
                    """ Se toma las horas de semana mas las hora en que retiro el servicio"""
                    if minuteEnd>0:
                        hoursWeekday= hoursWeekday + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
                elif weekDayEnd==7:
                    hoursWeekend= (24-hourStart)
                    """Se toma las horas desde que entro y el otro dia de fin de semana completo"""
                    hoursWeekday= (weekDayEnd-1)*24+ (24-hourEnd)
                    """ Se toma las horas de semana mas las hora en que retiro el servicio"""
                    if minuteEnd>0:
                        hoursWeekday= hoursWeekday + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
            
            
    def calcularPrecio(self, tarifa, tiempoDeServicio):
        """"Tarifa es un objeto en donde se guarda las tasas de cobranza"""
        """Tiempo de servicio es otro arreglo donde la primera posicion indica si es dia de semana """
        if tiempoDeServicio[0]==0 and tiempoDeServicio[1]==0:
            print("Hasta pronto")
            return 0
        tasaDiaDeSemana=tarifa.DiaSemana
        tasaFinDeSemana=tarifa.DiaFinDeSemana
        bsCobrar= tiempoDeServicio[0]* tasaDiaDeSemana + tiempoDeServicio[1]* tasaFinDeSemana
        print("Usted pagara un total de: ", bsCobrar)
        return



ahora = datetime.now() 
mas_5h = ahora + timedelta(hours=5)
mas_4d = ahora + timedelta(days=4)
mas_3d = ahora + timedelta(days=3)
print(ahora)
print(mas_5h)
print(mas_4d)
tarifa = Tarifa()
tarifa.DiaSemana=100
tarifa.DiaFinDeSemana=200
Calcular=Calculo()
tiempo_Servicio= Calcular.tiempoDeTrabajo(mas_3d, mas_4d)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)


  