import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create the app

external_stylesheets = [dbc.themes.BOOTSTRAP]
workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
request_path_prefix = None
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'
    
app = dash.Dash(__name__,
                requests_pathname_prefix=request_path_prefix,
                external_stylesheets=external_stylesheets)

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_csv('Activos.csv', delimiter=';', encoding='latin1')

# ------------------------------------------------------------------------------

#App Layout    
app.layout = html.Div([

    html.H1("EPM Dashboard", style={'text-align': 'center'}),
    
    dcc.Dropdown(id="asset_num",
                 options=[
                     {"label": "2976773", "value": 2976773},
                     {"label": "2976774", "value": 2976774},
                     {"label": "2976775", "value": 2976775},
                     {"label": "2976776", "value": 2976776},
                     {"label": "2976777", "value": 2976777},
                     {"label": "2976779", "value": 2976779},
                     {"label": "2976780", "value": 2976780}],
                 multi=False,
                 value=2976773,
                 style={'width': "40%"}
                 ),
    
    html.Div(id='asset', children=[]),
    html.Br(),

    html.Div(id='status', children=[]),
    html.Br(),
    
    html.Div(id='location', children=[]),
    html.Br(),
    
    html.Div(id='install_date', children=[]),
    html.Br(),
    
    html.Div(id='description', children=[]),
    html.Br(),

    dcc.Graph(id='my_graph', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='asset', component_property='children'),
     Output(component_id='status', component_property='children'),
     Output(component_id='location', component_property='children'),
     Output(component_id='install_date', component_property='children'),
     Output(component_id='description', component_property='children')],
     #Output(component_id='my_graph', component_property='figure')],
    [Input(component_id='asset_num', component_property='value')]
)
def update_output(asset):
    
    ass_status = df[df['ASSETNUM']==asset]['STATUS'][0]
    ass_location = df[df['ASSETNUM']==asset]['LOCATION'][0]
    ass_ins_date = df[df['ASSETNUM']==asset]['INSTALLDATE'][0] if df[df['ASSETNUM']==asset]['INSTALLDATE'][0] == df[df['ASSETNUM']==asset]['INSTALLDATE'][0] else "NA"
    ass_descr = df[df['ASSETNUM']==asset]['DESCRIPTION'][0]
    
    asset_num = "El número de activo es: {}".format(asset)
    status = "Estatus del activo: {} ".format(ass_status)
    location = "Localización: {}".format(ass_location)
    install_date = "Fecha de instalación: {}".format(ass_ins_date)
    description = "Descripción: {}".format(ass_descr)


    # Aquí va el código para la gráfica, no sé si podamos adicionar una imagen mientras

    return asset_num, status, location, install_date, description


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)