import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from plotly.subplots import make_subplots
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

def basic_plot(x=10, y=10):

    pic1 = go.Scatter(
            x = [i for i in range(x)],
            y = [i for i in range(x)],
            name = 'Index',
            marker = {'color':'green'}
        )

    pic2 = go.Scatter(
            x = [i for i in range(y)],
            y = [i for i in range(y)],
            name = 'Vol',
            marker = {'color':'red'}
        )
    data = [pic1,pic2]
    layout = go.Layout(
            title= (f''),
            titlefont=dict(
            family='Courier New, monospace',size=15,color='#7f7f7f'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',

            yaxis=dict(
                title='%'
            ),
            xaxis=dict(
                title=''
            )

            )
    return go.Figure(data=data, layout=layout)

