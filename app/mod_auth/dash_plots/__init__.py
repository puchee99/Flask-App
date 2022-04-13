import sys
sys.path.append("..")
import sqlalchemy as db 
import pandas as pd
import dash
import glob
from sqlalchemy import create_engine

#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import flask_login
from library import SQL_query


from app.mod_auth.dash_plots import plot_figures 
df = SQL_query.df_from_db()

#fig2 = plot_figures.basic_plot(df['TSLA_Y'] ,df['TSLA_Vol'])bull marketT% recessionT%
fig2 = plot_figures.basic_plot(df['bull marketT%'] ,df['recessionT%'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def create_dash(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/auth/plots/')

    #dash_app.index_string = html_layout
    print(df['TSLA_Y'] ,df['TSLA_Vol'])
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

#https://dash.plotly.com/dash-html-components/button
#https://community.plotly.com/c/dash/16
#https://dash.plotly.com
#https://dash-gallery.plotly.host/Portal/
#https://github.com/davidcomfort/dash_sample_dashboard
#https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f








    """
    @dash_app.callback(
        dash.dependencies.Output('container-button-timestamp', 'children'),
        [dash.dependencies.Input('submit-val', 'n_clicks')],
        [dash.dependencies.Input('my-range-slider', 'value')],#(id, variable_que_agafes)
        [dash.dependencies.State('input-on-submit', 'value')])
    def update_output(_, stack, value = 'ALL'):#entenc que les agafa ordenades de adalt
        if value == 'ALL':
            comb_count = helper.get_range(data)#,'buffandas')#'ClickClickClick')
        else:
            comb_count = helper.get_range(data,value)
            #comb_count = helper.get_range(data, value)
        fig = plot_figures.allin_call_range(comb_count, stack = stack)
        #canviar funció per fer stack segons la barra min/max, i no els rangs ja assignats
        return dcc.Graph(
        id='example-graph-extra',
        figure=fig
        )
    """
    

    """
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = flask_login.login_required(dash_app.server.view_functions[view_function])
    """

   
"""
name_db = 'Start_DF'
try: 
    engine = create_engine(f"sqlite:///{name_db}.sqlite")
    df1.to_sql(name_db, con=engine)
except:
    print('table exists')
"""