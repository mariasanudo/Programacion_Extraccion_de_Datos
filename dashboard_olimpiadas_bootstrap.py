import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table, callback, Input, Output

# dcc -------- Dash Core Components (componentes de interaccion)
# html ------- Das Html Components (componentes de html)

data = pd.read_csv("datasets/data_olimpiadas.csv", index_col= 0)

def tarjeta_filtros():
    control = dbc.Card([
        html.Div([
            dbc.Label("Genero: "),
            dcc.Dropdown(options= ["ALL","MALE","FEMALE"], value= "ALL")
        ]),
        html.Div([
            dbc.Label("Medal: "),
            dcc.Dropdown(options=["all", "gold", "silver", "bronze"], value="all", id="ddMedal")
        ]),
        html.Div([
            dbc.Label("Year: "),
            dcc.Input(type= "number", min= 1946, max= 2023)
        ])
    ])
    return control

def dashboard():
    data_pais = data.groupby("country", as_index= False).sum(numeric_only= True)
    g1 = px.line(data_pais, x= "country", y= ["gold","silver","bronze"])
    body = html.Div(children= [
        html.H2("Datos olimpiadas"),
        html.P("Objetio Dashboard: Mostarr los resultados de las medallas de los países"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H3("Filtros"),
                        tarjeta_filtros()
                    ]), width= 3
                ),
                dbc.Col(
                    html.Div([
                        dbc.Row(dcc.Graph(figure= g1, id= "figMedal")),
                        dbc.Row(dash_table.DataTable(data= data.to_dict("records"), page_size=10))
                    ]), width= 9
                )
            ], align= "center"
        )
    ])
    return body

if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets= [dbc.themes.CYBORG])
    app.layout = dashboard()
    app.run(debug= True)

