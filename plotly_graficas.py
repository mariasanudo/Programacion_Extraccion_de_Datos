import pandas as pd
import plotly.express as px

data = pd.read_csv("datasets/weekly_stocks.csv", parse_dates= True)
#print(data.head())
fig = px.line(data, x="Date", y="MSFT", title="Microsoft Store")
fig_box = px.box(data, y=["MSFT","AAPL"], title="Grafica de caja y bigotes")
fig_area = px.area(data, x="Date", y=["MSFT","AAPL","FB"], title="grafica de area")

data["Date"] =  pd.to_datetime(data["Date"])
data2 = data.set_index("Date")
data_3month = data2.resample(rule="M").mean()[-3:]
data_3month = data_3month.reset_index()
#print(data_3month)

columnas = ["MSFT","AAPL","FB"]
fig_bar = px.bar(data_3month, x = "Date", y= columnas, title="Grafica de barras")
fig_bar.update_layout(xaxis_title= "Mes", yaxis_title= "Dolar", title= "Stocks mensuales")

nbins= int(len(data)**(1/2))
#print(nbins)
fig_hist = px.histogram(data, x="Date", y="MSFT", title="Microsoft Store", nbins= 20)

fig_disp = px.scatter(data, x="Date", y="MSFT", title="Microsoft Store", size= "MSFT", color= "Date")

df_iris = px.data.iris()
#print(df_iris.sample(5))
fig_iris = px.scatter(df_iris, x= "species", y= "petal_width", size= "petal_length", color= "species")

df_tips = px.data.tips()
#print(df_tips.sample(5))
fig_pie = px.pie(df_tips, values= "total_bill", names= "day")
fig_pie.show()

#fig.show()
#fig_box.show()
#fig_area.show()
#fig_bar.show()
#fig_hist.show()
#fig_disp.show()
#fig_iris.show()