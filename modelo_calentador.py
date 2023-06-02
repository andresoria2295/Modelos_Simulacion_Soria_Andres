'''
---Calentador de Agua---
Forma: Cilindrica
Material: Polietileno
Capacidad = 1L
Espesor = 1cm
Altura = 25cm
Radio = 8cm

necesito calcular el calor que pierde y la potencia perdida de un dispositivo hueco
cilíndrico de polietileno con capacidad de 1 litro, espesor de 1 cm, altura de 25 cm y
radio de 5 cm con una temperatura interior de 50°C y temperatura exterior de 30°C.

'''

#!/usr/bin/python3
import random
import math
import matplotlib.pyplot as graph
graph.style.use('ggplot')

def grafico(temp_sp, temp_cp, cronometro_total):
    figure = graph.figure()
    figure.set_size_inches(30,30)
    graph.subplot(1,2,1)
    graph.xlabel('Ticks [s]')
    graph.ylabel("Grados [°C]")
    #for Ti in range (len(listado_temp_s)):
    #    graph.plot(listado_temp_s[Ti], label='Ti:'+str(Ti))
    graph.plot(cronometro_total, temp_sp)
    graph.title("Curva sin pérdida")
    graph.subplot(1,2,2)
    graph.xlabel('Ticks [s]')
    graph.ylabel("Grados [°C]")
    #for Ti in range (len(listado_temp_c)):
    #    graph.plot(listado_temp_c[Ti], label='Ti:'+str(Ti))
    graph.plot(cronometro_total, temp_cp)
    graph.title("Curva con pérdida")
    graph.legend()
    graph.show()

def calorPerdido(k,area_ext,area_int,espesor,deltaT):
    Qint = (k*area_int*deltaT)/espesor
    Qext = (k*area_ext*deltaT)/espesor
    QTotal = (Qint + Qext)
    return QTotal

def main():
    V = 220 #Tensión de fase [V].
    R = 48.3995 #Resistencia en fase [ohm].
    Vbateria = 12 #Tensión de batería. [V]
    Rbateria = 0.144 #Resistencia de batería. [ohm]
    Qs = 1 #Calor a entregar 1 [KJ/s]
    m = 1 #Masa [kg]
    Qesp = 4.186
    Qesp_alt = 4186 #[J/s]
    Ti = 25 #Temperatura inicial e interior [C].
    Tf = 0 #Temperatura final [C].
    vol = 1 #[m3]
    temp_sp = []
    temp_cp = []
    cronometro_total = []

    k = 0.4 #Resistividad térmica [W/m·K]
    radio_ext = 0.08 #[m]
    espesor = 0.01 #[m]
    h = 0.25 #[m]
    #area_int = 0.1257 #[m2]
    #area_ext = 0.1571 #[m2]
    Tint = 25 #Temperatura interior [C]
    Text = 25 #Temperatura exterior [C]
    cronometro = 0

    print('\n----------Calentador de Agua----------\n')
    print('\n A continuación, se simulará un modelo de calentador de agua con los siguientes parámetros/condiciones iniciales:')
    mensaje = """
    Forma: Cilíndrica
    Material: Polietileno
    Capacidad = 1L
    Espesor = 1cm
    Altura = 25cm
    Radio = 8cm
    """
    print(mensaje)
    #calcular las areas y q, luego el resto ya hecho.
    '''
    for i in range(1):
        Vbat = random.uniform(10, 14.4)
        Vbat = round(Vbat,4)
        print('Tensión de batería: '+str(Vbat)+' V.')

    R = V/I
    Rbateria = Vbateria/Ibateria
    R = round(R,4)
    Rbateria = round(Rbateria,4)
    print('Resistencia a 220 V = '+str(R)+' ohm.')
    print('Resistencia a 12 V = '+str(Rbateria)+' ohm.')
    '''
    print('\nTensión = '+str(V)+' V.')
    print('\nResistencia a 220 V = '+str(R)+' ohm.')

    #Calculo de corriente.
    I = V/R
    Ibateria = Vbateria/Rbateria
    #Round redondea el valor decimal de un número a su entero más cercano.
    I = round(I,4)
    Ibateria = round(Ibateria,4)
    print('\nCorriente a 220 V = '+str(I)+' A.')
    #print('Corriente a 12 V = '+str(Ibateria)+' A.')

    #Cálculo de potencia.
    P = (pow(V,2))/R  #Potencia equivalente a Qs = 1000 [J/s]
    potencia = round(P,4)
    print('\nPotencia a 220 V = '+str(potencia)+' W.\n')
    print('\n Cálculo de área interna y externa del elemento/dispositivo cilíndrico:\n')
    radio_int = radio_ext - espesor
    constante_pi = math.pi
    area_int = 2*constante_pi*radio_int*h
    areaI = round(area_int,4)
    print('\nÁrea interna del cilindro: '+str(areaI)+' m2.')
    area_ext = 2*constante_pi*radio_ext*h
    areaE = round(area_ext,4)
    print('\nÁrea externa del cilindro: '+str(areaE)+' m2.\n')

    while True:
        cronometro += 1
        #Cálculo de temperatura del agua sin pérdida.
        #Qs = m * Qesp * (Tf - Ti)
        Tf = (Qs/(m*Qesp))+Ti
        temp_sp.append(Ti)
        Ti_mostrar = round(Ti,4)
        print('\nPara '+str(cronometro)+'s - Temp. Final s/pérdida: '+str(Ti_mostrar)+'°C')
        #T_alt = calculoAlternoT(P,m,Qesp_alt,Ti)
        Ti = Tf
        deltaT = Tint - Text
        QTotal = calorPerdido(k,area_ext,area_int,espesor,deltaT)

        #Cálculo de temperatura del agua con pérdida.
        Tint = Tint + (P - QTotal)/Qesp_alt
        temp_cp.append(Tint)
        Tint_mostrar = round(Tint,4)
        #P = QTotal/deltaT
        print('\nPara '+str(cronometro)+'s - Temp. Final c/pérdida: '+str(Tint_mostrar)+'°C')
        cronometro_total.append(cronometro)
        if (cronometro >= 550):
            break;

    grafico(temp_sp, temp_cp, cronometro_total)

if __name__ == '__main__':
    main()
