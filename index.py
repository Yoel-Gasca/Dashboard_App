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
            html.P('Selecciona el historial del crédito', className='fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(
                id='credit_history',
                labelStyle={'display': 'inline-block', 'margin-right': '20px'},
                options=[
                    {'label': 'Critical account', 'value': 'critical account/ other credits existing (not at this bank)'},
                    {'label': 'Existing credits', 'value': 'existing credits paid back duly till now'},
                    {'label': 'No credits taken', 'value': 'no credits taken/ all credits paid back duly'},
                    {'label': 'Delay in paying', 'value': 'delay in paying off in the past'}
                ],
                value='existing credits paid back duly till now',
                style={'text-align':'center', 'color':'black'}, 
                className='dcc_compon'
            ),
        ], className='create_container2 five columns', style={'margin-bottom': '20px'}),
    ], className='row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id='my_graph', figure={})
        ], className='create_container2'),

        html.Div([
            dcc.Graph(id='pie_graph', figure={})
        ], className='create_container2')
    ], className='row flex-display'),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', 'figure'),
    [Input('credit_history', 'value')]
)
def update_graph(value):
    filtered_df = df[df['credit_history'] == value]
    
    fig = go.Figure()

    # Agregar las barras para cada categoría de 'purpose'
    for purpose, data in filtered_df.groupby('purpose'):
        fig.add_trace(go.Histogram(
            x=data['purpose'],
            y=data['credit_amount'],
            name=str(purpose)
            #marker_color="#02aaf8" if purpose == 'NO' else "#023368"
        ))

    # Configura el diseño del gráfico
    fig.update_layout(
        title="Distribución del Monto del Crédito por Propósito",
        xaxis_title="Propósito",
        yaxis_title="Monto del Crédito",
        barmode='group',
        bargap=0.1
    )

    return fig

@app.callback(
    Output('pie_graph', 'figure'),
    [Input('credit_history', 'value')]
)
def update_graph_pie(value):
    filtered_df = df[df['credit_history'] == value]
    purpose_counts = filtered_df['purpose'].value_counts()
    
    fig2 = go.Figure()

    fig2.add_trace(go.Pie(
        labels=purpose_counts.index,
        values=purpose_counts.values,
        hole=0.2
       # marker=dict(colors=["#02aaf8", "#023368", "#abcdef", "#123456"])  # Colores personalizados opcionales
    ))

    fig2.update_layout(
        title=f'Distribución del Monto del Crédito por Propósito',
        width=600,
        height=400
    )

    return fig2

if __name__ == '__main__':
    app.run_server(debug=True)