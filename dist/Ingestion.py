import pandas as pd
import numpy as np
from tabulate import tabulate
def carga_datos():

    ordenes= pd.read_csv("../Historicos_Ordenes.csv")
    caracteristicas= pd.read_csv("../Caracteristicas_Equipos.csv")
    registros= pd.read_csv("../Registros_Condiciones.csv")

    return ordenes,caracteristicas, registros
