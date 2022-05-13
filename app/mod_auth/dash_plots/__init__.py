import sys
sys.path.append("..")
import sqlalchemy as db 
import pandas as pd
import dash
import glob
from sqlalchemy import create_engine

from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import flask_login


from app.mod_auth.dash_plots import plot_figures 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
fig2 = plot_figures.basic_plot()

def create_dash(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/plots/')

    #dash_app.index_string = html_layout
    dash_app.layout = html.Div(style=external_stylesheets, children=[
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
    ,
    dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=25,
        step=1,
        value=[10, 25],
        marks = {'style':{'width': '1vh', 'height': '1vh'}}
    ),
    html.Div(id='container-button-timestamp'),
    dcc.Graph(
        id='example-graph-1',
        figure=fig2
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=fig2
    )
]   )
    return dash_app

