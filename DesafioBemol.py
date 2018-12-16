
# coding: utf-8

# # DESAFIO BEMOL

# Willander Buraslan

# #Previamente, abri os arquivos no excel para inputar o cabeçalho na planilha "clientes" e entender os dados.
# #Transformei "," em "." e ";" em "," para gerar dois arquivos .csv
# #Fiz o upload dos arquivos no meu github para tornar o processo mais acessível e identificar erros, caso tivessem.
# #A partir daí, passei a trabalhar no Jupyter Notebook.

# In[56]:


#importei as bibliotecas necessárias
import pandas as pd
import numpy as np


# In[57]:


#Abri o arquivo bonus através do link do mesmo no github e após transforma-lo em um arquivo .csv
bonus = pd.read_csv("https://raw.githubusercontent.com/WillanderBuraslan/DesafioBemol/master/bonuslimpo.csv")
print(bonus.head())


# In[58]:


#Abri o arquivo clientes através do link do mesmo no github e após transforma-lo em um arquivo .csv
clientes = pd.read_csv("https://raw.githubusercontent.com/WillanderBuraslan/DesafioBemol/master/clienteslimpo.csv")
print(clientes.head())


# In[59]:


#Identifiquei a quantidade de linhas e de colunas para verificar se os arquivos estavam compatíveis, no caso sim
print(bonus.shape)
print(clientes.shape)


# In[60]:


#Fiz o merge dos dois arquivos, nesse caso instituí o parametro cliente para left on e right on
#Coloquei o arquivo bonus como fixo e inclui o arquivo clientes depois
dados = bonus.merge(clientes, left_on='cliente', right_on='cliente', how='outer')


# In[61]:


#Imprimí a tabela com o merge entre os dois arquivos
print(dados)


# In[62]:


#Acrescentei uma nova coluna na planilha dados e somei as colunas saldo+historico
dados['saldo_historico'] = dados['saldo'] + dados['historico']


# In[63]:


#Imprimi a nova tabela com a ultima coluna sendo o saldo historico
#os valores da ultima coluna são a soma entre o saldo e o historico de cada cliente
print(dados)


# In[77]:


dados.reset_index().to_csv('DADOSexportados.csv' , header=True , index=False) 


# In[78]:


print("Muito Obrigado!")

