# Import packages

import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, Input, Output, callback, html, dash_table, dcc
import pandas as pd
from pprint import pprint
import numpy as np  
import json

import dash_ag_grid as dag
import os

from importlib import reload
from src.bank_transaction_analyser import BankTransactionAnalyser as bank
from src.bank_transaction_reader import BankTransactionReader as btr


# Initialize app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG]
)


darkMode=True
def dym(class_name, darkMode=darkMode):
    return class_name + ' dark-theme' if darkMode else class_name

table_bg = '#17202A' if darkMode  else '#F8F9F9'
table_fontColor = '#F2F3F4' if darkMode  else '#515A5A'
dash_config = {'displayModeBar': False}


def unpack_data(jsonlike_data):
    df = pd.read_json(jsonlike_data, orient='split')
    return df

# Incorporate data
res = os.listdir('bank-statement')
files=['bank-statement/' + i for i in res if i.endswith('.pdf')]

df = btr.read(files)
banker = bank(df, darkmode=darkMode)

# App layout ================================================================================
app.layout = dbc.Container([
    dbc.Card(dbc.CardBody([
        dcc.DatePickerRange(
                        id='input-date-range',
                        min_date_allowed=df.Date.min(),
                        max_date_allowed=df.Date.max(),
                        initial_visible_month=df.Date.mean(),
                        start_date=df.Date.min(),
                        end_date=df.Date.max(),
                        display_format='MMM Do, YY'
                        ),
        html.Button('Reset', id='reset', className='button-30')
    ])),
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dcc.Tabs(id='main-tab',value='balance',
                         parent_className=dym('custom-tabs'),
                         children=[
                    dcc.Tab(label='Balance', value='balance',
                            className=dym('custom-tab'),
                            selected_className=dym('custom-tab--selected'),
                            children=[
                        html.Label('BALANCE LEVEL OVERTIME'),
                        dcc.Graph(id='timeline-balance',config=dash_config)
                    ]),
                    dcc.Tab(label='Spending', value='spending', 
                            className=dym('custom-tab'),
                            selected_className=dym('custom-tab--selected'),
                            children=[
                        html.Label('CATEGORISED SPENDINGS'),
                        dcc.Graph(id='timeline-spending',config=dash_config)
                    ]),
                ])
            ])
        ])
    ]),
    dbc.Card(dbc.CardBody([
            # header here
            html.Label(children='TRANSACTION', style={'text-align':'center'}),
            # server side update is easy just leave this bank container.
            dbc.Row([
                dbc.Col([
                    dash_table.DataTable(
                        id='output-table', 
                        data=[], 
                        page_size=10,
                        # filter_action="native",
                        # filter_query='',#! these two does not work if there is no column 
                        style_header={
                            'backgroundColor':table_bg ,
                            'color': table_fontColor,
                            'fontWeight': 'bold'
                        },
                        style_data={
                            'backgroundColor': table_bg,
                            'color': table_fontColor
                        },
                        style_filter={
                            'backgroundColor': table_bg,
                            'color': table_fontColor
                        },
                        style_table={'overflowX': 'auto'}
                    )
                ])
            ])
    ])),
    # Cache Transformed Data
    dcc.Store(id='relevant-data')
])

# Server ==================================================


@callback(
    (Output('input-date-range', 'start_date'),
    Output('input-date-range', 'end_date')),
    Input('reset', 'n_clicks')
)
def reset_date(n):# reset button
    n
    return (df.Date.min(), df.Date.max())
    
@callback(
    Output('relevant-data', 'data'),# is a cache store
    Input('input-date-range', 'start_date'),
    Input('input-date-range', 'end_date')# data filtering
)
def caching_data(start, end):# filtering data based on input date
    filtered_data=df.query('Date >= @start & Date <= @end')
    jsonfield_data=filtered_data.to_json(date_format='iso', orient='split')
    return jsonfield_data

@callback(
    (Output('output-table', 'data'),
    Output('output-table', 'columns'),
    Output('output-table','filter_action')
    ),
    Input('relevant-data', 'data')
)
def update_table(json_data) -> list[dict]:
    dff=unpack_data(json_data)
    table_data=dff.to_dict('records')
    columns=dff.columns
    return (table_data,[{"name": i, "id": i} for i in columns],'native')

@callback(
    Output('timeline-balance', 'figure'),
    Input('relevant-data','data')
)
def update_balance_plot(jsonlike_data):
    df=unpack_data(jsonlike_data)
    banker.update_data(df)
    fig = banker.plotly_balance()
    return fig

@callback(
    Output('timeline-spending', 'figure'),
    Input('relevant-data','data')
)
def update_spending_plot(jsonlike_data):
    df=unpack_data(jsonlike_data)
    banker.update_data(df)
    if (df.Date.max() - df.Date.min()).days > 50:
        period='Month' 
        type='bar'
    else:
        period='Week'
        type='line'

    fig = banker.plotly_spending_period(period,type=type)
    return fig

#Run the app
if __name__ == '__main__':
    app.run(debug=True)

