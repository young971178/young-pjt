import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

file_path = 'iris.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')

df.hist(figsize=(10, 8), layout=(2, 2), edgecolor='black')
plt.tight_layout()
plt.show()
