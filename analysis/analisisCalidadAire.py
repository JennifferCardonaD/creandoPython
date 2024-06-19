import pandas as pd

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando un dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna","ica", "fecha", "id"])
    dataFrameICA.to_csv("datosIca.csv",index=False)
    print(dataFrameICA)

construirDataICA()