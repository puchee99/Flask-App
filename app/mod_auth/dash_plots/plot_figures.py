import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
#import backend.helper as helper

from plotly.subplots import make_subplots
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

def basic_plot(x, y):

    pic1 = go.Scatter(
            x = [i for i in range(len(x))],
            y = x,
            name = 'Index',
            marker = {'color':'green'}
        )

    pic2 = go.Scatter(
            x = [i for i in range(len(y))],
            y = y,
            name = 'Vol',
            marker = {'color':'red'}
        )
    data = [pic1,pic2]
    layout = go.Layout(
            title= (f'Stock'),
            titlefont=dict(
            family='Courier New, monospace',size=15,color='#7f7f7f'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',

            yaxis=dict(
                title='%'
            ),
            xaxis=dict(
                title='stack (BB)'
            )

            )
    return go.Figure(data=data, layout=layout)


"""
def create_template(list_plots_names,**kwargs):
    fichier_html_graphs=open("DASHBOARD.html",'w')
    fichier_html_graphs.write("<html><head></head><body>"+"\n")

    if 'hero_and_vilian' in list_plots_names:
        list_plots_names.remove('hero_and_vilian')
        list_plots_names.append('hero_push_vilian')
        list_plots_names.append('vilian_push_hero')

    for index,name in enumerate(list_plots_names):
        if name == 'hero_push_vilian':
            fig = fig_allin_push(kwargs['betallin'], kwargs['callallin'],'hero')
        elif name == 'vilian_push_hero':
            fig = fig_allin_push(kwargs['betallin'], kwargs['callallin'],'vilian')
        elif name == 'cards':
            fig = freq_parts_hands(kwargs['data_hands'], action = False)
        elif name == 'avg_player_win':
            fig = average_gain_player(kwargs['all_general'])
        elif name == 'allin_call_range':
            fig = allin_call_range(kwargs['comb_count'][0], stack = kwargs['comb_count'][1])


        plotly.offline.plot(fig, filename='Chart_'+str(index)+'.html',auto_open=False)
        fichier_html_graphs.write("  <object data=\""+'Chart_'+str(index)+'.html'+"\" width=\"650\" height=\"500\"></object>"+"\n")
    fichier_html_graphs.write("</body></html>")


def freq_parts_hands(df, action = False):
    freq_action = df[['num_players', 'has_flop', 'has_turn', 'has_river', 'has_show_down']].groupby('num_players').mean()
    title = 'Frequency of reaching parts of a hand ' 
    if action != False:
        title +=  " ".join(action.split("_")[1:]) + ' is seen'
    data = []
    fig = go.Figure()
    for i in [3,2]:
        sub = freq_action.loc[i]
        if action == 'has_flop':
            sub = sub/sub[action]
            sub = sub.drop(action)
        elif action == 'has_turn':
            sub = sub/sub[action]
            sub = sub.drop(['has_flop',action])
        elif action == 'has_river':
            sub = sub/sub[action]
            sub = sub.drop(['has_flop','has_turn',action])

        data.append(
            go.Bar(
                x = sub.index,
                y = sub.round(3).values,
                name = f'{i} players'
            )
        )
    layout = go.Layout(
            title= (title),
            yaxis=dict(
                range=(0,1)
            )
            )
    return go.Figure(data=data, layout=layout)

def fig_allin_push(betallin,callallin,name):
    if name == 'hero':
        bet = betallin['hero']
        name_push  = 'Hero PUSH'
        name_call  = 'Vilain CALL'
        call = callallin['vilain']
    else:
        bet  = betallin['vilain']
        name_call  = 'Hero CALL'
        name_push  = 'Vilian PUSH'
        call  =  callallin['hero']
    pic1 = go.Scatter(
            x = ['stack: '+ elmt for elmt in bet.index],
            y = (bet.round(3)*100).values,
            name = name_push,
            marker = {'color':'green'}
        )

    pic2 = go.Scatter(
            x = ['stack: '+ elmt for elmt in call.index],
            y = (call.round(3)*100).values,
            name = name_call,
            marker = {'color':'red'}
        )
    data = [pic1,pic2]
    layout = go.Layout(
            title= (f'{name_push} vs {name_call}'),
            titlefont=dict(
            family='Courier New, monospace',size=15,color='#7f7f7f'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',

            yaxis=dict(
                title='%'
            ),
            xaxis=dict(
                title='stack (BB)'
            )

            )
    return go.Figure(data=data, layout=layout)

def average_gain_player(all_general):
    from itertools import compress
    #bool_index = [i if 'cache_pos_puchito_9909' in i.keys() else False for i in all_general ]
    #num_index = list(compress(range(len(bool_index )), bool_index )) 
    c = [elm for elm in all_general if 'cache_pos_puchito_9909' in elm.keys()]   
    d = [elm for elm in c if 'hero_hand' in elm.keys()] 
    player_summary = pd.DataFrame([{
    'tournament': elmt['tournament_number'],
    'hand': helper.make_hand(elmt['hero_hand']),
    'gain': elmt['cache_puchito_9909_gain'],
    'bb': elmt['big_blind'],
    'stack': helper.binarize(elmt['cache_puchito_9909_bankroll']),
    'position': elmt['cache_pos_puchito_9909']}   for elmt in d ]) #'position': elmt['cache_pos_puchito_9909']}  for elmt in all_general]#'gain': elmt['cache_hero_gain']
            #if 'hero_hand' in elmt.keys()

    player_summary['gain_chips'] = player_summary['gain']*player_summary['bb']
    chips_win = player_summary.groupby(['tournament','bb'])[['gain','gain_chips']].sum().reset_index()
    data = []

    for bb in [20,30,40,60,80,100]:
        sub = chips_win[chips_win['bb'] == bb]['gain_chips'].cumsum()
        
        data.append(
            go.Scatter(
                x = list(range(len(sub))),
                y = sub.values,
                name = str(bb)
            )
        )
    layout = go.Layout(
            title= ('Average gain by BB over time')
            )
    return go.Figure(data=data, layout=layout)

def allin_call_range(comb_count, stack = [0,25]):
    m = [x for x in range(stack[0],stack[1])]
    current_range = list(comb_count[_] for _ in m)
    vilain_range = current_range[0]
    for rangeX in current_range[1:]:
        for key_hand in rangeX.keys():
            vilain_range[key_hand] += rangeX[key_hand]

    FIGURES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    FIGURES.reverse()

    df_range = pd.DataFrame(columns = FIGURES, index = FIGURES)
    for k,v in vilain_range.items():
        c1,c2,s = k
        if s == 's':
            df_range.loc[c2,c1] = v
        else:
            df_range.loc[c1,c2] = v
            
    df_range = df_range.fillna(0)

    colors  =[[0.0, "rgb(165,0,38)"],
                [0.1111111111111111, "rgb(215,48,39)"],
                [0.2222222222222222, "rgb(244,109,67)"],
                [0.3333333333333333, "rgb(253,174,97)"],
                [0.4444444444444444, "rgb(254,224,144)"],
                [0.5555555555555556, "rgb(224,243,248)"],
                [0.6666666666666666, "rgb(171,217,233)"],
                [0.7777777777777778, "rgb(116,173,209)"],
                [0.8888888888888888, "rgb(69,117,180)"],
                [1.0, "rgb(49,54,149)"]]
    colors.reverse()
    data = [go.Heatmap(z=np.round(df_range),x=FIGURES,
            y=FIGURES,colorscale=colors)]#='Inferno')]#["white","red","purple"])]
            
    layout = go.Layout(
            title= (f'Opponent All-in Call Range {stack}BB '),
            xaxis = dict(side="top", title = 'Suited'),
            yaxis = dict(title = 'OffSuited',autorange='reversed'),
            height = 500, 
            width = 500,
            coloraxis_showscale=False,
            
    )
    return go.Figure(data=data, layout=layout)

"""