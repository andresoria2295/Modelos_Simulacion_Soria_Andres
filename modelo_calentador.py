'''
---Calentador de Agua---
Forma: Cilindrica
Material: Polipropileno
Capacidad = 1L
Espesor = 1cm
Altura = 20 cm
Radio = 4cm
'''

#!/usr/bin/python3
import random
import matplotlib.pyplot as graph
graph.style.use('ggplot')

def grafico(listado_temp_s, listado_temp_c):
    figure = graph.figure()
    figure.set_size_inches(30,30)
    graph.subplot(1,2,1)
    graph.xlabel('Ticks')
    #for Ti in range (len(listado_temp_s)):
    #    graph.plot(listado_temp_s[Ti], label='Ti:'+str(Ti))
    graph.plot(listado_temp_s, label='Curva sin pérdida')
    graph.title("Temperaturas")
    graph.subplot(1,2,2)
    graph.xlabel('Ticks')
    #for Ti in range (len(listado_temp_c)):
    #    graph.plot(listado_temp_c[Ti], label='Ti:'+str(Ti))
    graph.plot(listado_temp_c, label='Curva con pérdida')
    graph.title("Temperaturas")
    graph.legend()
    graph.show()

def calculoAlternoT(P,m,Qesp,Ti):
    Tf = 0
    Tf = (P/(m*Qesp))+Ti
    return Tf

def calorPerdido(k,area_ext,area_int,espesor,deltaT):
    Qint = (k*area_int*deltaT)/espesor
    Qext = (k*area_ext*deltaT)/espesor
    QTotal = Qint + Qext
    return QTotal

def main():
    P = 1000 #potencia equivalente a Qs = 1000 [J/s]
    V = 220 #tensión de fase
    Vbateria = 12 #tensión de batería
    Qs = 1 #calor a entregar 1 [KJ/s]
    m = 1 #masa
    Qesp = 4.186
    Qesp_alt = 1 #[J/s]
    Ti = 25 #temperatura inicial e interior [C]
    Tf = 0 #temperatura final
    vol = 1
    lista_temp_s = []
    lista_temp_c = []

    k = 0.15 #resistividad térmica [W/m·K]
    area_int = 0.0377 #[m2]
    area_ext = 0.0503 #[m2]
    temp_ext = 25 #temperatura exterior [C]
    espesor = 0.01 #[m]
    contador = 0

    print('\n---Calentador de Agua---\n')

    for i in range(1):
        Vbat = random.uniform(10, 14.4)
        Vbat = round(Vbat,4)
        print('Tensión de batería: '+str(Vbat)+' V.')

    #Calculo de corriente y resistencia
    I = P/V
    Ibateria = P/Vbateria
    #Round redondea el valor decimal de un número a su entero más cercano.
    I = round(I,4)
    Ibateria = round(Ibateria,4)
    print('Corriente a 220 V = '+str(I)+' A.')
    print('Corriente a 12 V = '+str(Ibateria)+' A.')
    print('\n')

    R = V/I
    Rbateria = Vbateria/Ibateria
    R = round(R,4)
    Rbateria = round(Rbateria,4)
    print('Resistencia a 220 V = '+str(R)+' ohm.')
    print('Resistencia a 12 V = '+str(Rbateria)+' ohm.')
    print('\n')

    while True:
        #Qs = m * Qesp * (Tf - Ti)
        Tf = (Qs/(m*Qesp))+Ti
        #Tf = (P/(m*Qesp))+Ti
        lista_temp_s.append(Ti)
        print('Para '+str(contador)+'s - Temp. Final s/pérdida:'+str(Ti)+'°C')
        T_alt = calculoAlternoT(P,m,Qesp_alt,Ti)
        Ti = Tf
        contador += 1
        deltaT = temp_ext - T_alt #Invertido
        QTotal = calorPerdido(k,area_ext,area_int,espesor,deltaT)
        print("Calor perdido: ", QTotal)
        P = QTotal/deltaT
        Tfp = (QTotal/(m*Qesp))+T_alt
        lista_temp_c.append(Tfp)
        print('Para '+str(contador)+'s - Temp. Final c/pérdida: '+str(Tfp)+'°C')
        if (Ti >= 100):
            break;
    print('\n')
    #print(lista_temp)
    print('\n')
    grafico(lista_temp_s, lista_temp_c)

if __name__ == '__main__':
    main()
