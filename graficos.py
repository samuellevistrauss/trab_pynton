import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# DataFrame do Banco de dados
Dados = pd.read_excel('dados.xlsx')

# DataFrame da qntd de pessoas/cidade
DPC = Dados.groupby('Cidade ').size()

# DataFrame da qntd de pessoas/graduação
DPG = DVR.groupby('Graduação').size()

# DataFrame da qntd de faixa pretas
DFPVR = DVR[DVR['Graduação']=='Preta']

# mostra o gráfico da quantidade de atletas nos bairros de volta redonda
DVRbairros.groupby('Bairro').size().plot(kind='bar', figsize=(16,6), colormap='Blues_r')
