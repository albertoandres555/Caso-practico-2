

import pandas as pd
import numpy as np
from tabulate import tabulate

def limpieza(df):
    if 'Fecha' in df.columns:
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        print("columna:Fecha cambiado su tipo a Datetime" )
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
        print("columna:"+col+"cambiado su tipo de object a category" )
    return



registros.dropna(inplace=True)


registros[registros.duplicated()]

z_scores = (registros.select_dtypes(include=[np.number])-registros.select_dtypes(include=[np.number]).mean(numeric_only=True))/registros.select_dtypes(include=[np.number]).std(numeric_only=True)
z_scores_abs = z_scores.apply(np.abs)
umbral = 3
out_mask = ~z_scores[z_scores_abs > umbral].isna()
print(out_mask.sum())
outliers = registros['Temperatura_C'][out_mask['Temperatura_C']]
outliers

# %% [markdown]
# BORRO LOS 30 OUTLIERS

# %%
registros.drop(outliers.index,inplace=True)
registros.info()

# %% [markdown]
# CARDINALIDAD

# %%
def calc_cardinalidad(adf):
    result = {}
    for col in adf.columns:
        print('\n- Valores únicos para "{0}"'.format(col), '\n')
        # print(adf[col].unique())
        card = len(adf[col].unique())
        print('Num valores únicos: ', len(adf[col].unique()))
        result[col] = card
    return result
registros_card = calc_cardinalidad(registros)
print(registros_card)

# %%
for col in registros.columns:
    print('frecuencia para: "{0}"'.format(col),"\n")
    print(registros[col].value_counts())

# %%
registros.describe()

# %% [markdown]
# ANALISIS DE CORRELACION

# %%
registros.corr(method="pearson",numeric_only=True)

# %% [markdown]
# ANALISIS SESGO

# %%
registros_skw=registros.skew(numeric_only=True)
registros_skw

# %% [markdown]
# KURTOSIS

# %%
registros_kurt = registros.kurt(numeric_only=True)
registros_kurt

# %% [markdown]
# PROFILING

# %%
#! pip install ydata-profiling


# %%
from ydata_profiling import ProfileReport
profile = ProfileReport(registros, title="Registros_Profiling_Report")
profile.to_notebook_iframe()
profile.to_file('Registros_profile_report.html')

