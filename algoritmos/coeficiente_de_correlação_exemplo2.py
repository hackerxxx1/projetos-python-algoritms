# -*- coding: utf-8 -*-
"""coeficiente de correlação exemplo2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n3zsnO7vxz38LLhbirRzJv9ZXT7zzy0b
"""

# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 5

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
data = {'criança':[1,2,3,4,5,6,7,8,9,10,11,12],
        'aptmat':[60,58,73,51,54,75,48,72,75,83,62,52],
        'aptmus':[80,62,70,83,62,92,79,88,54,82,64,69]}
df = pd.DataFrame(data,columns = ['criança', 'aptmat', 'aptmus'])
Corr = df.corr()
print(Corr)
sn.heatmap(Corr, annot=True)
plt.show()