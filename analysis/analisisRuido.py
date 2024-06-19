import pandas as pd

from generators.generadorDecibelios import generaDatoRuido

def construirDataRuido():
    #creando un dataFrame
    datosRuido=generaDatoRuido()
    dataFrameRuido=pd.DataFrame(datosRuido,columns=["id","nivelRuido","comuna"])
    dataFrameRuido.to_csv("datosRuido.csv",index=False)
    print(dataFrameRuido)

construirDataRuido()

