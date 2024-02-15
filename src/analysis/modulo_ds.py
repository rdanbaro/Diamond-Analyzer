
# ## Importaciones

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Funcion utilizada en el apply para buscar habito con mas dias consecutivos
def count_consecutive_yes(series):
    max_consecutive_yes = 0
    current_consecutive_yes = 0
    for value in series:
        if value == 'Yes':
            current_consecutive_yes += 1
            max_consecutive_yes = max(max_consecutive_yes, current_consecutive_yes)
        else:
            current_consecutive_yes = 0
    return max_consecutive_yes


def get_datos_metas(ruta):
    datos = pd.read_csv(ruta)

    list_objs = [i.strip() for i in list(datos['Pendientes'])]
    list_requisito = list(datos['Requisito'].fillna(1))
    list_cumplido =  list(datos['Cumplido'].fillna(0))
    list_realizado = [True if i.strip() == 'Yes' else False for i in list(datos['Realizado'])]
    
    
    
    return list_objs, list_requisito, list_cumplido, list_realizado 
    
def dame_graficas(ruta):
    data_habit_example = pd.read_csv(ruta)
    me_interesa_d = data_habit_example.drop(columns=['Progress', 'Status', 'Day']).iloc[len(data_habit_example)-12:len(data_habit_example)]
    me_interesa = data_habit_example.drop(columns=['Date','Progress', 'Status', 'Day']).iloc[len(data_habit_example)-12:len(data_habit_example)]


    #Habito mayor&menor frecuencia
    frec_habit = me_interesa.eq('Yes').sum()
    dict = frec_habit.to_dict()
    habits_maxfrec = [i for i in list(dict.keys()) if dict[i] == frec_habit.max()]
    habits_minfrec = [i for i in list(dict.keys()) if dict[i] == frec_habit.min()]
    habits_ordenados = frec_habit.sort_values()


    #Frecuencia x dia
    new_name = me_interesa.transpose().reset_index()

    new_name.columns = range(13)
    frec_dia = new_name.eq('Yes').sum()

    dict_d = frec_dia.to_dict()
    days_maxfrec = [i for i in list(dict_d.keys()) if dict_d[i] == frec_dia.max()]
    days_minfrec = [i for i in list(dict_d.keys()) if dict_d[i] == frec_dia.min()]




    #Maximos dias consecutivos
    consecutive_yes_count = me_interesa.apply(count_consecutive_yes)

    dict_r = consecutive_yes_count.to_dict()
    habits_maxrach = [i for i in list(dict_r.keys()) if dict_r[i] == consecutive_yes_count.max()]

    #Porcentaje de dias cumplidos
    me_interesa.eq('Yes').sum().sum()
    habits_porcent = me_interesa.eq('Yes').sum().sum() / me_interesa.size * 100


    #GRAFICAR
    colors = sns.color_palette("deep")
    fig, ax = plt.subplots(1, 2, figsize=(7, 3))
    fig.set_facecolor('#a8dadc')
    # Filtrar los datos para excluir los días con contador 0
    frec_dia_filtrado = frec_dia[frec_dia.values != 0]

    # Convertir los índices en cadenas
    frec_dia_filtrado.index = frec_dia_filtrado.index.astype(str)

    # Graficar un gráfico de barras en el primer eje
    ax[0].bar(frec_dia_filtrado.index, frec_dia_filtrado.values, alpha=0.75, color='#2a9d8f')
    ax[0].set_title('Hábitos por día')
    ax[0].set_xlabel('Numero del Día')
    ax[0].set_ylabel('Frecuencia')

    # Graficar un gráfico de líneas en el segundo eje
    ax[0].plot(frec_dia_filtrado.index, frec_dia_filtrado.values, alpha=0.85)


    frec_habit_filtrado = habits_ordenados[habits_ordenados.values != 0]
    #colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
    ax[1].barh(frec_habit_filtrado.index, frec_habit_filtrado.values, color=colors )
    ax[1].set_title('Total dias cumplidos ')
    ax[1].set_xlabel('Cantidad total de dias')
    ax[1].set_ylabel('Hábitos')
    ax[1].set_xticks(range(0,16,2))

    # Ajustar el diseño de las subtramas
    plt.tight_layout()

    return fig