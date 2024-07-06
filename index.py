import dash
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import plotly.figure_factory as ff

df = pd.read_csv ('Dashboard_App\Data\german_credit.csv')
#print(df)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    html.Div([
        html.H1('German Bank'),
        html.Img(src='assets/img/BankAppLogo2.png')
    ], className = 'banner'),
])

if __name__ == ('__main__'):
    app.run_server(debug=True)