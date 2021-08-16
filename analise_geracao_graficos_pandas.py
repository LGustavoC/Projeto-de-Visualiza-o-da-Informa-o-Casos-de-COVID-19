#!pip install plotly
# importações e leitura de arquivo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
Casos = pd.read_csv('arquivo_geral_covid.csv', sep=';')
Casos.head()

# Barras Horizontais
y = Casos.groupby("regiao").casosNovos.sum(
).sort_values(ascending=False).head(20)
plt.figure(figsize=(5, 10))
plt.barh(y.index, y.values, color='blue', edgecolor='cyan')
plt.yticks(y.index, size=8)
plt.xlabel('Casos Novos')
plt.ylabel('Região')
plt.show()


# Barras Verticais
casos = Casos.groupby("estado").obitosNovos.sum().sort_values(ascending=False)
plt.figure(figsize=(20, 8))
plt.bar(casos.index, casos.values, color='blue', edgecolor='cyan')
plt.xticks(casos.index, size=8)
plt.ylabel('Óbitos Novos')
plt.xlabel('Estados')
plt.show()


# Pizza
sort_genre = Casos.groupby('regiao', as_index=False)['obitosAcumulados'].count().rename(col
plt.rcParams["figure.figsize"]=(16, 10)
group_size=sort_genre['count'].values.tolist()
group_labels=sort_genre['regiao'].values.tolist()
plt.pie(group_size, autopct=lambda p: '{:.2f}% ({:.0f})'.format(p, p * sum(group_size)/100),
fig=plt.gcf()
plt.title('Número de Registros Por Região', fontsize=18);


# Histograma
cN=Casos.groupby('data').casosNovos.sum()
cA=Casos.groupby('data').casosAcumulados.sum()
oN=Casos.groupby('data').obitosNovos.sum()
oA=Casos.groupby('data').obitosAcumulados.sum()
plt.figure(figsize=(20, 15))
plt.grid()
plt.plot(cN.index, n.values, label='Casos Novos')
plt.plot(cA.index, j.values, label='Casos Acumulados')
plt.plot(oN.index, e.values, label='Óbitos Novos')
plt.plot(oA.index, o.values, label='Óbitos Acumulados')
plt.xticks(n.index, rotation='vertical', size=10)
plt.legend()
plt.ylabel('Casos e óbitos')
plt.xlabel('Data')
