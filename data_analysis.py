import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obtendo o caminho para os dados usando a variável de ambiente DATA_PATH
data_path = os.environ.get('DATA_PATH')

# print(data_path)

# Verificando se a variável de ambiente foi definida
if not data_path:
    raise ValueError('A variável de ambiente DATA_PATH não foi definida.')

# Criando o caminho completo para o arquivo de dados
# file_path = os.path.join(data_path, 'seu_arquivo_de_dados.csv')

df = pd.read_csv(data_path)

print(df.head())

plt.bar(df['nome'], df['pontuação'])
# plt.plot(df['nome'], df['pontuação'], marker='o', linestyle='-')
plt.title('Vendas ao longo dos anos')
plt.xlabel('Nome')
plt.ylabel('Pontuação')
plt.grid(True)
plt.show()
