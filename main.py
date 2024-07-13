import numpy as np

temperaturas = np.array([22, 21, 19, 18.5, 20.3, 25, 1])

media_temperatura = np.mean(temperaturas)
print(f"Média das temperaturas: {media_temperatura:.2f}ºC")

max_temperatura = np.max(temperaturas)
min_temperatura = np.min(temperaturas)
print(f"Temperatura máxima: {max_temperatura}ºC")
print(f"Temperatura mínima: {min_temperatura}ºC")

altas_temperaturas = temperaturas[temperaturas > 21]
print(f"Temperaturas acima de 21ºC: {altas_temperaturas}")