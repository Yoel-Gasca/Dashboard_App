import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('Dashboard_App\Data\german_credit.csv')
print(df)

