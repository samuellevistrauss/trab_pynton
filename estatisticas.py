import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# DataFrame do Banco de dados
Dados = pd.read_excel('dados.xlsx')

# DataFrame da qntd de pessoas/graduação
DPG = DVR.groupby('Graduação').size()

# DataFrame da qntd de faixa pretas
DFPVR = DVR[DVR['Graduação']=='Preta']

# mostra o box-plot dos faixa pretas de volta redonda
DFPVR[['Idade', 'Bairro']].plot.box()
