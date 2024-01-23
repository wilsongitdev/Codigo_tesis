from ..ads1115 import *
from ..gpio import GPIO

def ads1115_get_vprom():
    ##########3
        #algoritmo detectar flanco de bajada
        #print('foto almacenada')
        matr = []
        vez = 0
        t = 5
        fs = 32
        muestras = ((fs*t))
        ads1115config('A0', str(fs))##frecuencia de muestreo 16,32,64,128,250
        estado = 0
        while True: 
            #lee pulso
            if estado == 0:
                if GPIO.input(4) == True:
                    estado = 1
                else:
                    estado = 0
            
            if estado == 1:
                if GPIO.input(4) == True:
                    estado = 1
                else:
                    estado = 2
                    
            if estado == 2:
                estado = 3		
                #leer gpio
                databits = ads1115conv()
                matr.append(databits)
                #print('{:.7f}'.format(voltaje))
                vez=vez+1
                
                    
                
            if estado == 3:
                if vez==muestras:
                    vez=0
                    break
                else:
                    estado=0
        ###calcular el promedio#promedio a 0.5s

        dprom = sum(matr)/len(matr)
        vprom = dprom * 4.096/32767.0
        return matr, vprom
