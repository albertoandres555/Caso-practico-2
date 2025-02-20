import pandas as pd
import numpy as np
from tabulate import tabulate

def limpieza(df):
#Si hay columna Fecha cambio de tipo a datatime
    if 'Fecha' in df.columns:
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        print('columna: "Fecha" cambiado su tipo a Datetime')
#Si hay columnas Object cambio de tipo a category  
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
        print('columna: "'+str(col)+'", cambiado su tipo de object a category' )
    
#Busqueda de Nan y borrado
    numero_nan_x_colum=df.isna().sum()
        
    for col  in numero_nan_x_colum.index:
        if numero_nan_x_colum[col]>0:
            print(f"Columna '{col}' tiene {numero_nan_x_colum[col]} valores NaN. Eliminando Nan de esta columna.")
            df.dropna(inplace=True)

#Busqueda de duplicados y borrado
    num_dupli=df[df.duplicated()].count().values[0]
    if num_dupli>0:
        df.drop_duplicates(inplace=True)
        print('Eliminando '+str(num_dupli)+' duplicados\n')
   

#z-scores calculo y borrado
    z_scores = (df.select_dtypes(include=[np.number]) - df.select_dtypes(include=[np.number]).mean(numeric_only=True)) / df.select_dtypes(include=[np.number]).std(numeric_only=True)
    z_scores_abs = z_scores.apply(np.abs)
    umbral = 3
    out_mask = z_scores_abs > umbral

    for col in out_mask.columns:
        if out_mask[col].any():
            print(f'Outliers en la columna: "{col}" : {out_mask[col].sum()}, todos eliminados')
            outliers = df[col][out_mask[col]]
            df.drop(outliers.index, inplace=True)

#Resumen despues de limpieza
    print("\nTAMAÑO:", df.shape,"\n\nRESUMEN:")
    print(tabulate(df.describe(),headers='keys'))

#CARDINALIDAD   
    result = {}
    for col in df.columns:
        #print('\n- Valores únicos para "{0}"'.format(col))
        card = len(df[col].unique())
        #print('Num valores únicos: ', len(df[col].unique()))
        result[col] = card
    print('\nCARDINALIDAD:\nNumero de valores únicos por cada columna:',result,"\n")

    for col in df.columns:
        print('frecuencia para: "{0}"'.format(col))
        print(df[col].value_counts(),"\n")
#CORRELACION
    df_correlacion=df.corr(method="pearson",numeric_only=True)
    print("Correlación: Se considera que hay correlacion para valores mayores de 0,7")
    print(tabulate(df_correlacion,headers='keys'))
#SKEW
    df_skew=df.skew(numeric_only=True)
    print("\nSkew (analizar si ha valores mayores de 2 (o -2):)")
    print(df_skew)
#KURTOSIS
    df_kurt = df.kurt(numeric_only=True)
    print ("\nKurtosis, (analizar si ha valores mayores de 3 (o -3):)")
    print(df_kurt)
#PROFILING
    print("\nPROFILING\n")
    from ydata_profiling import ProfileReport
    profile = ProfileReport(df, title="Profiling_Report")
    profile.to_notebook_iframe()
    profile.to_file('Profile_report.html')
    
    return df