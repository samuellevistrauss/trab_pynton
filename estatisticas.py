import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# DataFrame do Banco de dados
Dados = pd.read_excel('dados.xlsx')

# DataFrame da qntd de pessoas/graduação
DPG = pd.read_excel('DPG.xlsx')

# DataFrame da qntd de faixa pretas
DFPVR = pd.read_excel('DFPVR.xlsx')

# mostra o box-plot dos faixa pretas de volta redonda
DFPVR[['Idade', 'Bairro']].plot.box()
