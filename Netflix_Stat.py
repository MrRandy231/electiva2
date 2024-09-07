# SALUDOS PROFESOR JUAN RESTITUYO
# RANDY JAVIER MOTA DIVISON - 2021-0812 

import pandas as pd
import matplotlib.pyplot as plt
    

netflix_df = pd.read_csv('netflix_titles.csv')

print(netflix_df.head(10))
print(netflix_df.tail(15))
print(netflix_df.describe())

netflix_df.fillna(0, inplace=True)

# DATOS BÁSICOS
movies_and_series_df = netflix_df[(netflix_df['type'].isin(['Movie', 'TV Show'])) & (netflix_df['release_year'] >= 2010)]


# GRAFICOS AGRUPADOS

grouped_df = movies_and_series_df.groupby(['release_year', 'type']).size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(12,6))
bar_width = 0.35
opacity = 0.8

# BARRA DE PELICULAS
rects1 = ax.bar(grouped_df[grouped_df['type'] == 'Movie']['release_year'], 
                grouped_df[grouped_df['type'] == 'Movie']['count'], 
                bar_width, 
                alpha=opacity, 
                color='b', 
                label='Películas')

# BARRA DE SERIES
rects2 = ax.bar(grouped_df[grouped_df['type'] == 'TV Show']['release_year'] + bar_width, 
                grouped_df[grouped_df['type'] == 'TV Show']['count'], 
                bar_width, 
                alpha=opacity, 
                color='g', 
                label='Series')

# LABELS, TITULOS Y LEYENDAS DEL GRAFICO
ax.set_xlabel('Año')
ax.set_ylabel('Número de títulos')
ax.set_title('Películas vs Series en Netflix (2010-2021)')
ax.set_xticks(grouped_df['release_year'].unique())
ax.legend()

plt.show()





