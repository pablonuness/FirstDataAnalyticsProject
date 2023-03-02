#!/usr/bin/env python
# coding: utf-8

# #  0.Introdução

# Análise de dados em relação aos jogos lançados entre os anos 1980 - 2020 que foram disponibilizados através do site www.kaggle.com.
# 
# O objetivo é evidenciar pontos em questão das colunas e contagens possíveis e, a partir disso, elaborar propostas para tais acontecimentos.
# 
# Link do Dataset:
# https://www.kaggle.com/datasets/gregorut/videogamesales

# # 1.Carregando bibliotecas

# In[1]:


import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# # 2.Carregando Dataset

# In[2]:


VG  = pd.read_csv('vgsales.csv',index_col='Rank')


# In[3]:


VG.shape


# In[4]:


VG.info()


# In[5]:


VG.head(5)


# # 3.Análise univariada

# In[6]:


_ = plt.hist(VG.Year)
_ = plt.title('Histograma de Lançamentos por Ano')


# Através deste histograma é enaltecido que até o ano de 2020 ocorreram certas explosões de Lançamentos de games, com maiores localizados entre os anos de 2005 e 2010.

# In[7]:


VG.Publisher.value_counts().head(10)


# In[8]:


VG.Genre.value_counts().head(10)


# In[9]:


VG.Platform.value_counts().head(10)


# In[10]:


_ = VG.Genre.value_counts().plot.bar()
_ = plt.title('Produção por Gênero')


# Podemos notar que a maior categoria de games produzidas é de Action que é uma categoria de games mais casuais(Assim como Misc e Role-Playing), sem envolver tanta competitividade, assim estimulando a compra de gamers que costumam jogar em tempo livre ou apenas por lazer, logo após podemos ver categorias que tem um nível elevado de competitividade envolvida, como Sports e Shooter.

# # 4.Análise Bivariada

# In[11]:


_ = sns.boxplot(x='Year',y='Genre',data=VG)


# Através deste gráfico é possível notar que com o passar do tempo os jogos de Action acabaram perdendo sua aparição, por diversos fatores, destacando-se o fato de que muitos estavam ligados aos primeiros consoles lançados e aos fliperamas que hoje em dia estão diminuindo em número.

# In[12]:


_ = sns.scatterplot(x='Year',y='Global_Sales', data = VG)


# Pode-se notar que a concentração de vendas está na atualidade e que é um mercado cada vez mais próspero.

# # 5.Análise multivariada

# In[13]:


VG.corr()

