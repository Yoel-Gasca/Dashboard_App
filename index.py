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

     html.Div([
        html.Div([
            html.P('Selecciona el historial del credito', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'credit_history', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Critical account', 'value' : 'critical account/ other credits existing (not at this bank)'},
                                {'label' : 'Existing credits', 'value' : 'existing credits paid back duly till now'},
                                {'label' : 'No credits taken', 'value' : 'no credits taken/ all credits paid back duly'},
                                {'label' : 'delay in paying', 'value': 'delay in paying off in the past'}
                            ], value = 'historial_de_credito',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):

    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame = df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph_pie(value):

    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'primera_dosis_cantidad')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'segunda_dosis_cantidad'
        )
    return fig2

if __name__ == ('__main__'):
    app.run_server(debug=True)