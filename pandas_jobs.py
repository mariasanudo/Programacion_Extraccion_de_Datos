import pandas as pd

jobs = pd.read_csv("datasets/Jobs.csv", index_col=0)
#print(jobs.head(10)) #los primeros
#print(jobs.sample(10)) #aleatorios
#print(jobs.describe()) #estadistica, resumen
print(jobs.info) #tipo de datos