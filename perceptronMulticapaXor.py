import numpy as np
import math 
import matplotlib.pyplot as plt

matrizEntrada = np.matrix([[0,0],
                           [0,1],
                           [1,0],
                           [1,1],])
matrizSalidas = np.matrix([[-1,1,1,-1]]).T

numeroNeuronas = 30

matrizPesosCapaOculta =  np.matrix(np.random.uniform(-1.0,1.0,(numeroNeuronas,2)))
matrizUmbralCapaOculta=  np.matrix(np.random.uniform(-1.0,1.0,(numeroNeuronas,1)))
matrizPesosCapaSalida =  np.matrix(np.random.uniform(-1.0,1.0,(1,numeroNeuronas)))
matrizUmbralCapaSalida=  np.matrix(np.random.uniform(-1.0,1.0,(1,1)))

vectorError = []
alfa = 0.001

for i in range(0, 10000):   
     sum=0
     for j in range(0, len(matrizEntrada)):   
        tempCalculoSalida= matrizPesosCapaOculta*matrizEntrada[j].T  + matrizUmbralCapaOculta
        salidaCapaOculta= np.tanh(tempCalculoSalida)    
       
        tempCalculoSalidaFinal= matrizPesosCapaSalida*salidaCapaOculta + matrizUmbralCapaSalida 
       
        salidaCapaOcultaFinal =np.tanh(tempCalculoSalidaFinal)
       
        error = matrizSalidas[j] - salidaCapaOcultaFinal
        sum += error.item(0)*error.item(0)
        
        funcionActivacionCapaFinal = -2*error * (1- np.multiply(salidaCapaOcultaFinal ,salidaCapaOcultaFinal))
        funcionActivacionCapaOculta = 1 - np.multiply(salidaCapaOculta,salidaCapaOculta)
        funcionActivacionCapaOculta = np.diag(funcionActivacionCapaOculta.A1)
        funcionActivacionCapaOculta =funcionActivacionCapaOculta * matrizPesosCapaSalida.T * funcionActivacionCapaFinal 


        matrizPesosCapaSalida = matrizPesosCapaSalida - alfa * funcionActivacionCapaFinal * salidaCapaOculta.T
        matrizUmbralCapaSalida= matrizUmbralCapaSalida - alfa * funcionActivacionCapaFinal

        s = matrizEntrada[j].T
        matrizPesosCapaOculta = matrizPesosCapaOculta - alfa * funcionActivacionCapaOculta * s.T
        matrizUmbralCapaOculta = matrizUmbralCapaOculta - alfa * funcionActivacionCapaOculta
     vectorError.append(sum/4)


for j in range(0, len(matrizEntrada)):   
        tempCalculoSalida= matrizPesosCapaOculta*matrizEntrada[j].T  + matrizUmbralCapaOculta
       
        salidaCapaOculta= np.tanh(tempCalculoSalida)
       

       
        tempCalculoSalidaFinal= matrizPesosCapaSalida*salidaCapaOculta + matrizUmbralCapaSalida 
        
        salidaCapaOcultaFinal =np.tanh(tempCalculoSalidaFinal)           
        print(matrizSalidas[j])
        print(round(salidaCapaOcultaFinal.item(0),0))




plt.subplot(1,2,1)
plt.plot(vectorError)
plt.ylabel('numeros')
plt.show()


