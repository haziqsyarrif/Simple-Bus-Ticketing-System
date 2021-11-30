#Visualisasi Data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

N = 3
ind = np.arange(N)  

df = pd.read_csv("manifest_1.csv")
df['Destinasi'].value_counts().plot(kind='bar')
plt.ylabel("Tiket Terjual")
plt.xlabel("Destinasi Tujuan")
plt.show()

df['Waktu'].value_counts().plot(kind='bar')
plt.ylabel("Frekuensi Dipilih")
plt.xlabel("Waktu Keberangkatan")
plt.xticks(ind, ('06.00', '13.00', '18.30'))
plt.show()

df['Tempat Duduk'].value_counts().plot(kind='bar')
plt.ylabel("Frekuensi Dipilih")
plt.xlabel("Tempat Duduk")
plt.show()

