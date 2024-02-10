
# ## Importaciones

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
def get_datos_metas(ruta):
    datos = pd.read_csv(ruta)

    list_objs = [i.strip() for i in list(datos['Pendientes'])]
    list_requisito = list(datos['Requisito'].fillna(1))
    list_cumplido =  list(datos['Cumplido'].fillna(0))
    list_realizado = [True if i.strip() == 'Yes' else False for i in list(datos['Realizado'])]
    
    

    return list_objs, list_requisito, list_cumplido, list_realizado 
    





