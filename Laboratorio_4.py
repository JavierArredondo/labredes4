"""
Laboratorio 3 de Redes de Computadores por Shalini Ramchandani & Javier Arredondo
Parte 2

"""
###################################################
################## Importaciones ##################
###################################################
import numpy as np
from numpy import linspace, pi, cos
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from scipy.fftpack import fft, ifft

import warnings
warnings.filterwarnings('ignore')

"""
Implementación de de modulación por desplazamiento de amplitud  [Amplitude-shift keying (ASK)]:
Es una forma de modulación en la cual se representan los datos digitales como variaciones de amplitud de la onda portadora en función de los datos a enviar.
La amplitud de una señal portadora analógica varía conforme a la corriente de bit (modulando la señal), manteniendo la frecuencia y la fase constante. 
El nivel de amplitud puede ser usado para representar los valores binarios 0s y 1s. Podemos pensar en la señal portadora como un interruptor ON/OFF. 
En la señal modulada, el valor lógico 0 es representado por la ausencia de una portadora, así que da ON/OFF la operación de pulsación y de ahí el nombre dado. 
La técnica ASK también es usada comúnmente para transmitir datos digitales sobre la fibra óptica. 
Para los transmisores LED, el valor binario 1 es representado por un pulso corto de luz y el valor binario 0 por la ausencia de luz.
"""

# FUNCIONES
"""
Función que se encarga de abrir archivos .wav y obtiene la frecuencia e información de la señal.
Entrada:
        name-> nombre del archivo con extensión .wav
Salida:
        rate  -> frecuencia de muestreo.
        info  -> datos de la señal.
        times -> tiempo para cada dato en info.
"""
def openWav(name):
        rate, info = read(name)
        dimension = info[0].size
        if(dimension == 1):
                data = info
        else:
                data = info[:,dimension-1]
        n = len(data)
        Ts = n / rate
        times = np.linspace(0, Ts, n)
        return (rate, data, times)

def intToBin(num, bits):
        numBin = format(num, "b").zfill(bits)
        if(numBin[0] == "-"):
                return "1"+numBin[1:]
        return numBin

def sizeBin(maxi):
        return len(format(maxi, "b")) + 1
        

def arrayToBin(signal):
	dataBin = []
	bits = sizeBin(max(signal))
	for data in signal:
                _bin = intToBin(data, bits)
                for i in _bin:
                        dataBin.append(int(i))
        return dataBin

def ASKmodulation(signal):
        A = 5
        B = 2

        timeASK = linspace(0, 1, 100)
        amplASK = cos(2 * pi * timeASK)

        ASK = []
        
        signalBin = arrayToBin(signal)
        for i in  signalBin:
                if(i == 1):
                        ASK.append(A * amplASK)
                else:
                        ASK.append(B * amplASK)                    
                        
        return


print("Start")
print(intToBin(9, 10))
print(intToBin(-9, 10))   
