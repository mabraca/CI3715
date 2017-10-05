from datetime import datetime, time, timedelta
'''
Created on 3/10/2017
@author: Maria Bracamonte 10-11147 Abelardo Salazar 13-11303
'''

class Tarifa:
    pass

class Calculo:
    """Clase Calculo calculara informacion 
    de la informacion dada"""
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
            raise ValueError("Error en los datos")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """Si el dia de servicio supera mas de siete dias"""
        if dayEnd-dayStart>7 or monthEnd!=monthStart or yearEnd!=yearStart:
            raise ValueError("El maximo de dias para el servicio ha superado el limite")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """ Ha utilizado menos de 15 minutos del servicio""" 
        if minuteEnd-minuteStart<15 and hourEnd==hourStart and dayEnd==dayStart and monthEnd==monthStart:
            raise ValueError("Ha tardado menos de 15 minutos, vayase gratis")
            pagar.append(0)
            pagar.append(0)
            return pagar
        """Si el servicio es del mismo dia"""
        if dayEnd==dayStart:
            """si hay mas de 15 minutos de diferencia pero en horas distintas mismo dia. """
            #if hourStart!=hourEnd 
            if (hourStart==hourEnd or hourEnd==hourStart +1) and (minuteEnd+(60-minuteStart))+((hourEnd-hourStart-1)*60)>15 and weekDayStart<6:
                """Si solo dura entre 15 a 59 minutos en dia de semana"""
                pagar.append(1)
                pagar.append(0) 
                return pagar
            if (hourStart==hourEnd or hourEnd==hourStart +1) and (minuteEnd+(60-minuteStart))+((hourEnd-hourStart-1)*60)>15  and weekDayStart>5:
                """Si solo dura entre 15 a 59 minutos en fines de semana"""
                print("paso por aqui")
                pagar.append(0)
                pagar.append(1) 
                return pagar
            """De lo contrario hago cuentas de cuantas horas dure durante el dia """
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
            if weekDayStart<5 and  weekDayEnd<6: 
                """Si el servicio empezo y termino en un dia de semana""" 
                firstday= 24-hourStart
                lastday= 24 - hourEnd
                hoursWeekday= (weekDayEnd - weekDayStart -1)*24            
                """ Cuantos dias enteros (24hr) se hizo el servicio """
                hoursWeekday= hoursWeekday + firstday + lastday 
                """El dia que se termino y que empezo no hizo 24hrs, solo los otros dias"""
                if minuteEnd>0:
                    hoursWeekday= hoursWeekday + 1          
                    """Si termino con un minuto mas de la hora se le suma otra hora"""
                
                pagar.append(hoursWeekday) 
                pagar.append(0)
                return pagar
            
            elif weekDayStart>5 and  weekDayEnd>5: 
                
                """Si el servicio empezo y termino en un fin de semana"""
                if dayStart == (dayEnd - 1):
                    """ Empezo sabado y termino domingo siguiente"""         
                    """ Me interesa las horas del sabado y las horas del domingo """
                    hoursWeekday= (24-hourStart) + (24-hourEnd)   
                    if minuteEnd>0:
                        hoursWeekday= hoursWeekday + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora"""
                    pagar.append(0)
                    pagar.append(hoursWeekday) 
                    return pagar
                else:
                    """ Empezo un domingo y termino el sabado siguiente"""  
                    hoursWeekday= (24-hourStart) + (24-hourEnd)
                    if minuteEnd>0:
                        hoursWeekday= hoursWeekday + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora"""
                    pagar.append(24*5)
                    pagar.append(hoursWeekday) 
                    return pagar
                    
            
            elif weekDayStart<6 and  weekDayEnd>5: 
                """Si el servicio empeza en un dia de semana y termino en un fin de semana""" 
                if weekDayEnd==6:
                    """Si empiezo cualquier dia de la semana y termino un sabado"""
                    firstday = 24-hourStart
                    hoursWeekend = 24-hourEnd
                    hoursWeekday= (weekDayEnd - weekDayStart -1)*24 + firstday
                    """Me interesa la hora del primer dia y el ultimo dia, el resto sera 24hr de dia de semana"""
                    if minuteEnd>0:
                        hoursWeekend= hoursWeekend + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
                elif weekDayEnd==7:
                    """Si empiezo cualquier dia de la semana y termino un domingo"""
                    firstday = 24-hourStart
                    hoursWeekday= (weekDayEnd - weekDayStart -2)*24 + firstday
                    """Resto dos porque debo descontar los dos dias de fin de semana"""
                    hoursWeekend= (24-hourEnd)+24
                    """dia de fin de semana trabajo uno completo y se le suma la hora del otro fin de semana"""
                    if minuteEnd>0:
                        hoursWeekend= hoursWeekend + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
            elif weekDayStart>5 and  weekDayEnd<6:
                """Si el servicio empezo en un fin de semana y termino en un dia de semana""" 
                firstday = 24-hourStart
                hoursWeekday= (weekDayEnd - weekDayStart -2)*24 + firstday
                if weekDayStart==6:
                    """Si empezo un sabado y termino en cualquier dia de la semana"""
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
                    """Si empezo un domingo y termino en cualquier dia de la semana"""
                    hoursWeekend= (24-hourStart)
                    """Se toma las horas desde que entro el domingo"""
                    hoursWeekday= (weekDayEnd-1)*24 + (24-hourEnd)
                    """ Se toma las horas de semana mas las hora en que retiro el servicio"""
                    if minuteEnd>0:
                        hoursWeekday= hoursWeekday + 1          
                        """Si termino con un minuto mas de la hora se le suma otra hora al la hora final"""
                    pagar.append(hoursWeekday)
                    pagar.append(hoursWeekend)
                    return pagar
            
            
    def calcularPrecio(self,tarifa, tiempoDeServicio):
        """"Tarifa es un objeto en donde se guarda las tasas de cobranza"""
        """Tiempo de servicio es otro arreglo donde la primera posicion indica si es dia de semana """
        self.tasaDiaDeSemana=tarifa.DiaSemana
        self.tasaFinDeSemana=tarifa.DiaFinDeSemana
        self.hrsSemanales = tiempoDeServicio[0]
        self.hrsFines = tiempoDeServicio[1]
        print("fines", self.hrsFines,"semanas",self.hrsSemanales)
        if tiempoDeServicio[0]==0 and tiempoDeServicio[1]==0:
            print("Hasta pronto")
            return 0
        
        bsCobrar= self.hrsSemanales* self.tasaDiaDeSemana + self.hrsFines* self.tasaFinDeSemana
        print("Usted pagara un total de: ", bsCobrar)
        return bsCobrar

ahora = datetime.now() 

tarifa = Tarifa()
tarifa.DiaSemana=100
tarifa.DiaFinDeSemana=200
Calcular=Calculo()
""" Caso0:  El mismo dia, y solo 25minutos en dia de Semana"""
print(" El mismo dia, y solo 25minutos en dia de Semana")
mas_min = ahora + timedelta(minutes=25)
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora, mas_min)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)

""" Caso1:  El mismo dia, y solo 25minutos en dia Fin de semana"""
print(" El mismo dia, y solo 25minutos en Fin de Semana")
ahora2= ahora + timedelta(days=3)
mas_min = ahora + timedelta(minutes=25) + timedelta(days=3)
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora2, mas_min)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)

""" Caso2: El mismo dia, y mas dos horas en dia de Semana"""
print("\n El mismo dia, y mas dos horas en dia de Semana")
mas_2hrs = ahora + timedelta(hours=2)
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora, mas_2hrs)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)

""" Caso3: dos dias despues y dos horas despues en dia de semanas"""
print("\n dos dias despues y dos horas despues en dia de semanas")
mas_2hrsfin = ahora + timedelta(days=2) +timedelta(hours=2)
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora, mas_2hrsfin)
print(tiempo_Servicio)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)

""" Cas4: Empieza en dia de semana y termina un Sabado"""
print("\n Empieza en dia de semana y termina un Sabado")
mas_3d = ahora + timedelta(days=3) 
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora, mas_3d)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)

""" Caso5:  Empieza en dia de semana y termina un Domingo"""
print("\n Empieza en dia de semana y termina un Domingo")
mas_3d = ahora + timedelta(days=3) 
tiempo_Servicio= Calcular.tiempoDeTrabajo(ahora, mas_3d)
Calcular.calcularPrecio(tarifa, tiempo_Servicio)