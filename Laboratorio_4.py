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
"""
Transformación de entero a binario, con n-bits
"""
def intToBin(num, bits):
        numBin = format(num, "b").zfill(bits)
        if(numBin[0] == "-"):
                return "1"+numBin[1:]
        return numBin
"""
Calculo de la cantidad de bits máximos que se deben ocupar
"""
def sizeBin(maxi):
        return len(format(maxi, "b")) + 1

"""
Transformacion de un arreglo de enteros a binario
"""
def arrayToBin(signal):
	dataBin = []
	bits = sizeBin(max(signal))
	for data in signal:
                _bin = intToBin(data, bits)
                for i in _bin:
                        dataBin.append(int(i))
	return dataBin

def graphDigitalData(binSignal, duration):
        binFixed = []
        for i in binSignal:
                for j in range(0, 10):
                        binFixed.append(i)
        print(len(binFixed))
        t = linspace(0, duration, len(binFixed))
        print(len(t))
        plt.plot(t[:1000], binFixed[:1000])
        plt.ylim(0, 2)
        plt.xlabel('Tiempo');
        plt.ylabel('Amplitud');
        plt.title('Señal Digital');
        plt.grid(True)
        plt.show()
        return

"""
Modulacion ASK
"""
def ASKmodulation(signal, bps, duration):
        A = 4  # Amplitudes de cada coseno
        B = 2
        f = 2  # Frecuencia de carrier
        timeCarrier = linspace(0, 1 - 1/bps, bps)   # Tiempo de un coseno, 1 seg, 100 muestras
        dataCarrier = cos(2 * pi * f * timeASK)     # Carrier: onda coseno
        
        signalBin = arrayToBin(signal) # Obtenemos un arreglo de los datos en binario de la señal original
        sizeBin = len(signalBin)       # Hay 1169808 elementos. Cantidad de bits totales en el audio.
        # Graficamos la señal digital
        graphDigitalData(signalBin, duration)
        
        cutBin = signalBin[0:10000] # Recortamos la muestra. Tomamos los 10000 primeros
        ASK = []
        for i in  cutBin:
                if(i == 1):
                        ASK = np.concatenate([ASK, (A * amplASK)])
                else:
                        ASK = np.concatenate([ASK, (B * amplASK)])
        t = linspace(0, duration, sizeBin * len(amplASK)) # Creamos un vector tiempo para graficar. Dura 9s con un total de muchos puntos.
        # Graficamos la señal modulada ASK
        plt.plot(t[0:10000], ASK[0:10000])
        plt.ylim(-6, 6)
        plt.xlabel('Tiempo')
        plt.ylabel('Amplitud')
        plt.title('Señal ASK')
        plt.grid(True)
        plt.show()
        return signalBin


print("Comienzo")
rate, data, times = openWav("handel.wav")
totalTime = len(data)/rate
t = linspace(0, totalTime, len(data))
ask = ASKmodulation(data, 100, totalTime)
