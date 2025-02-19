
import pandas as pd
import numpy as np
from tabulate import tabulate

def limpieza(df):
    if 'Fecha' in df.columns:
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        print('columna: "Fecha" cambiado su tipo a Datetime')
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
        print("columna: "+col+" ,cambiado su tipo de object a category" )
    

    numero_nan_x_colum=df.isna().sum()

    for col  in numero_nan_x_colum.index:
        if numero_nan_x_colum[col]>0:
            print(f"Columna '{col}' tiene {numero_nan_x_colum[col]} valores NaN. Eliminando los Nan de esta columna.")
            df.drop(columns=[col], inplace=True)

    
    df[df.duplicated()]




    return