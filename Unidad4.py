#Visualización
#Pandas graficas

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/weekly_stocks.csv", parse_dates= True, index_col= "Date")
#print(data.sample(5))

#GRAFICAS
#data.plot(y="MSFT",figsize =(9,6))
#data.plot.line(y="MSFT", title="Microsoft Stocks", ylabel="USD", xlabel="Week", color= "darkgreen")

#data.plot(kind= "box",vert=False)
#data.plot(kind= "area",y= ["MSFT","AAPL"])

#data.plot(kind= "area")
#data.plot(kind= "area",stacked=False) #TRANSPARENTA LOS COLORES PARA MOSTRAR LOS COLORES QUE SE SOBREPONEN

data_3month = data.resample(rule="M").mean()[-3:]
#data_3month.plot(kind="bar",ylabel="Price")
#data_3month.plot(kind="barh",ylabel="Price")

#data.plot(kind="hist",alpha=0.6,bins=25)

#data2 = data.reset_index()
#data2.plot(kind="scatter",x="Date",y="MSFT")

#data_3month.plot(kind="pie", subplots=True, legend=False, figsize=(14,7),autopct="%.f")
data_3month.MSFT.plot(kind="pie", figsize=(10,7),autopct="%.f")

plt.show()