# -*- coding: utf-8 -*-
"""Tratamento de Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Je7IBBROoxPQ7leEIh07Jj5JgupADFzL
"""

# Fabrício Santos Monteiro - 20114290072
# Gabriel Rodrigues - 20114290052
# Júlia Daphiny - 20114290029
# Caio Rodrigues - 20114290130
# Mayara Vieira - 19214290014

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

print(base)

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

# Definimos os previsores e classe
previsores = base.iloc[:, 0: 9].values
classe = base.iloc[:, 9].values

print(previsores)
print(classe)

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

# Definimos os previsores e classe
previsores = base.iloc[:, 0: 9].values
classe = base.iloc[:, 9].values

# Normalizar os dados dos previsores com o StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

print(previsores)

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

base.columns = [
                'idade',
                'escolaridade',
                'escolaridade_marido',
                'num_filhos',
                'religiao',
                'trabalhando',
                'profissao_marido',
                'estilo_de_vida',
                'exposicao_midia',
                'metodo_contraceptivo_usado',
]

# Definimos os previsores e classe
previsores = base.iloc[:, 0: 9].values
classe = base.iloc[:, 9].values

# Normalizar os dados dos previsores com o StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

# Criar o classificador
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()

classificador.fit(previsores, classe)

print('Propriedades da Tabela')
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

base.columns = [
                'idade',
                'escolaridade',
                'escolaridade_marido',
                'num_filhos',
                'religiao',
                'trabalhando',
                'profissao_marido',
                'estilo_de_vida',
                'exposicao_midia',
                'metodo_contraceptivo_usado',
]

# Definimos os previsores e classe
previsores = base.iloc[:, 0: 9].values
classe = base.iloc[:, 9].values

# Normalizar os dados dos previsores com o StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

# Treinar o modelo
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

# Criar o classificador
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()

classificador.fit(previsores_treinamento, classe_treinamento)

# Prever com base nos dados de teste
previsoes = classificador.predict(previsores_teste)

print('200 primeiros dados de teste', classe_teste[0:200])
print('200 primeiros dados previstos', previsoes[0:200])

import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)

# Lemos a base e vemos se tá tudo certo
base = pd.read_csv('cms.csv')

base.columns = [
                'idade',
                'escolaridade',
                'escolaridade_marido',
                'num_filhos',
                'religiao',
                'trabalhando',
                'profissao_marido',
                'estilo_de_vida',
                'exposicao_midia',
                'metodo_contraceptivo_usado',
]

# Definimos os previsores e classe
previsores = base.iloc[:, 0: 9].values
classe = base.iloc[:, 9].values

# Normalizar os dados dos previsores com o StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

# Treinar o modelo
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

# Criar o classificador
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()

classificador.fit(previsores_treinamento, classe_treinamento)

# Prever com base nos dados de teste
previsoes = classificador.predict(previsores_teste)

# Calcular métricas para saber a acurácia do algoritmo
from sklearn.metrics import confusion_matrix, accuracy_score

precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

print('- Algoritmo de ML com % de acerto de: ', round(100 * precisao, 2), '%')
print('\n- Matriz de erros e acertos: ')

# 1 = nenhum, 2 = 'longo prazo', 3 = 'curto prazo'
pd.DataFrame(matriz)