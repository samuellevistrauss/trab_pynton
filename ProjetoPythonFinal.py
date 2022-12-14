# -*- coding: utf-8 -*-
"""Cópia_de_Dados_estatistico_VR_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/samuellevistrauss/trab_pynton/blob/main/C%C3%B3pia_de_Dados_estatistico_VR_.ipynb

# Importação das Bibliotecas **Pandas** e **Matplotlib**
"""

import pandas as pd
import matplotlib.pyplot as plt

def post_execute():
  if matplotlib.is_interactive():
    draw_all()

"""# DataFrame 'Dados' gerado a partir do Banco de Dados (arq dados.xlsx)"""

Dados = pd.read_excel('/content/drive/MyDrive/dados.xlsx') # criando o DataFrame
Dados.head() # amostragem das 5 primeiras linhas do DataFrame...

"""# DataFrame 'DPC' com a quantidade de atletas/cidade"""

DPC = Dados.groupby('Cidade ').size() # criando uma matriz unidimensional com a quantidade de atletas/cidade
display(DPC) # amostragem das cidades não tratada

Dados['Cidade '].unique() # função mostra as entradas individuais (cidades) do DataFrame 'Dados'

"""## Tratamento dos Dados das Cidades

Como obtivemos respostas diferentes a respeito de algumas cidades, precisamos tratar os dados. Para tal, utilizamos as funções lambda e replace.
"""

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Volta redonda','Volta Redonda'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Volta Redonda ','Volta Redonda'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Volta redonda ','Volta Redonda'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Volta redonda','Volta Redonda'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Vassouras ','Vassouras'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Resende RJ ','Resende'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Barra mansa','Barra Mansa'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Angra dos reis','Angra dos Reis'))

Dados['Cidade '] = Dados['Cidade '].apply(lambda x: str(x).replace('Volta Redonda\xa0','Volta Redonda'))

"""## Resultados"""

DPC = Dados.groupby('Cidade ').size() # agrupa a quantidade de atletas a cada cidade
display(DPC) # amostragem das cidades tratada

Dados['Cidade '].unique() # mostrando novamente os valores individuais da matriz, agora, com os dados tratados

"""# Amostragem geral da quantidade de atletas/graduação"""

Dados.groupby('Graduação').size() # amostragem das graduações não tratada

Dados['Graduação'] = Dados['Graduação'].apply(lambda x: str(x).replace(' Roxa','Roxa')) # tratando os dados

Dados.groupby('Graduação').size() # amostragem das graduações tratada

"""## Salvando os dados tratados das Cidades e Graduações para um novo arquivo .xlsx"""

Dados.to_excel("Dados_Tratados.xlsx")

"""# DataFrame 'DVR' gerado a partir de Dados apenas de Volta Redonda

Vamos selecionar apenas os dados de Volta Redonda pois foi onde se obtever maior amostragem.
"""

DVR = Dados[Dados['Cidade ']=='Volta Redonda'] # selecionando apenas os atletas de VR
DVR.to_excel("DVR.xlsx") # salvando o DataFrame para um novo arquivo xlsx
DVR.head() # amostragem das 5 primeiras linhas do DataFrame...

DVR.groupby('Bairro').size() # amostragem da quantidade de atletas por bairro, na cidade de Volta Redonda

DVR.groupby('Bairro').size().plot(kind='bar', figsize=(18,6), colormap='Blues_r') # plotando o gráfico da amostragem, sem tratamento

"""## Tratamentos dos Dados dos Bairros"""

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Agua limpa','Água Limpa'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Água limpa','Água Limpa'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Agua Limpa','Água Limpa'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Belvedere','Jardim Belvedere'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Jardim Jardim Belvedere','Jardim Belvedere'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Jardim belvedere','Jardim Belvedere'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Jardim Vila Rica Tiradentes','Vila Rica Tiradentes'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Vila rica tira-dentes','Vila Rica Tiradentes'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Vila rica','Vila Rica Tiradentes'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Vila Rica Tiradentes tres pocos','Vila Rica Tres Poços'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Monte castelo','Monte Castelo'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Monte castelo ','Monte Castelo'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Monte Castelo ','Monte Castelo'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Morada da colina','Morada da Colina'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Retiro ','Retiro'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Santa cruz','Santa Cruz'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Santo agostinho','Santo Agostinho'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('santo agostinho','Santo Agostinho'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('São luis','São Luís'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('São lucas','São Lucas'))

DVR['Bairro'] = DVR['Bairro'].apply(lambda x: str(x).replace('Volta grande','Volta Grande'))

"""## Resultados"""

DVR.groupby('Bairro').size().plot(kind='bar', figsize=(18,6), colormap='Blues_r') # gráfico de barras da amostragem, agora, com dados tratados

DVR['Bairro'].unique() # amostragem das entradas individuais dos bairros (tratados, ou seja, sem repetição)

DVR.plot.scatter(x = 'Idade', y = 'Graduação', alpha = 1.0) ## gráfico de dispersão idade/graduação

"""Mais Tratamentos..."""

DVR['Em relação aos treinos, qual a sua frequência ?'] = DVR['Em relação aos treinos, qual a sua frequência ?'].apply(lambda x: str(x).replace('De 1 a 2 vezes por semana, De 2 a 3 vezes por semana','De 1 a 2 vezes por semana'))

DVR['Em relação aos treinos, qual a sua frequência ?'] = DVR['Em relação aos treinos, qual a sua frequência ?'].apply(lambda x: str(x).replace('De 4 a 5 vezes  por semana', 'De 4 a 5 vezes por semana'))

DVR['Em relação aos treinos, qual a sua frequência ?'] = DVR['Em relação aos treinos, qual a sua frequência ?'].apply(lambda x: str(x).replace('De 1  a 2 vezes   por semana', 'De 1 a 2 vezes por semana'))

DVR.plot.scatter(x = "Graduação", y = "Em relação aos treinos, qual a sua frequência ?", alpha = 1.0) # gráfico de dispersão graduação/frequência de treinos

"""# Amostragem da quantidade de atletas/graduação de Volta Redonda (DPG)"""

DPG = DVR.groupby('Graduação').size() # criando a amostragem com a qntd de atletas/graduação
display(DPG) # amostragem

DPG.plot(kind='bar', x='Graduação', y=0, figsize=(16,6), colormap='gray'); # plotando gráfico de barras atletas/graduação

"""## Salvando os dados da nova amostragem para um novo arquivo .xlsx"""

DPG.to_excel("DPG.xlsx")

"""# Amostragem da quantidade de atletas/gênero de Volta Redonda (DVRS)"""

DVRSEXO = DVR.groupby('Sexo').size() # criando a amostragem com a qntd de atletas/gênero
display(DVRSEXO) # amostragem não tratada

"""## Tratamento..."""

DVR['Sexo'] = DVR['Sexo'].apply(lambda x: str(x).replace('Femenino','Feminino'))

"""## Resultados"""

DVRSEXO = DVR.groupby('Sexo').size() # nova amostragem após o tratamento..
display(DVRSEXO) # amostragem tratada

DVRSEXO.plot(kind='bar', x='Sexo', y=0, figsize=(5,6), colormap='Accent'); # plotagem do gráfico de barras atletas/gênero

"""# DataFrame 'DFPVR' gerado a partir dos Faixas Pretas de Volta Redonda."""

DFPVR = DVR[DVR['Graduação']=='Preta'] # criando DataFrame de Faixas Pretas restringido a Volta Redonda
DFPVR.head() # mostrando as 5 primeiras linhas do DataFrame...

DFPVR.groupby('Bairro').size() # distribuição dos Faixas Pretas de Volta Redonda por Bairro...

"""## Salvando os dados da nova amostragem dos Faixa Pretas de VR para um novo arquivo .xlsx"""

DFPVR.to_excel("DFPVR.xlsx")

"""# Análise Estatística dos Faixas Pretas de Volta Redonda"""

DFPVR[['Nome', 'Idade', 'Há quanto anos treina Jiu-Jitsu. ', 'Está há quanto anos na graduação atual ']] # Exibe o DataFrame com as colunas selecionadas

"""## Média de Idades"""

DFPVR['Idade'].mean()

"""## Média de tempo que treinam Jiu-Jitsu"""

DFPVR['Há quanto anos treina Jiu-Jitsu. '].mean()

"""## Média de quantos anos estão na graduação"""

DFPVR['Está há quanto anos na graduação atual '].mean()

DFPVR[['Idade']].plot.box() # gráfico bot-plot dos Faixas Pretas de Volta Redonda
