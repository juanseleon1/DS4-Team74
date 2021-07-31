import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
app.title = 'Epm Dashboard'

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(className='all',
    children=[
        html.Div(className='header', children=[
            html.Div(className='container_header',children=[
                html.Img(src='/assets/contratacion-distrito-termico.png',width=170,height=100),
                html.Div(className='header_title',children=[
                    html.H1(className='title_dashboard',children='Assets Dashboard'),
                    html.Img(className='logo_correlation_one',src='assets/Sin título.png')
                ]),
            ]),
            html.Div(className='bar_header')

        ]),
        html.Div(className='body_board',children=[
            html.Div(className='vertical_menu',children=[
                html.Div(className='container_vertical',children=[
                    dcc.Tabs(
                        id="tabs",
                        className='container_tab',
                        value='tab-1',
                        children=[
                            dcc.Tab(
                                label='Historical',
                                value='tab-1',
                                className='custom-tab',
                                selected_className='custom-tab--selected'
                            ),
                            dcc.Tab(
                                label='Extract Text',
                                value='tab-2',
                                className='custom-tab',
                                selected_className='custom-tab--selected'
                            ),
                        ])
                ])
            ]),
            html.Div(id='container_query')
        ]),
        html.Div(className='footer')
    ]
)

@app.callback(
    Output('container_query', 'children'),
    Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div(className='render_container_query',children=[
                html.H2(className='title_query',children='Assets  Number'),
                html.Div(className='container_query',children = [
                    html.Br(),
                    dcc.Input(id="input1",className='input', type="text", placeholder="", style={'marginRight': '10px'}),
                    html.Img(src='assets/search.png',width=32,height =32),
                    html.Div(id="output"),
                ]),
                html.Button('Search', id='button',className='button'),
            ]),
            html.Div(className='container_attribute',children=[
#                html.H2('Estatus'),
#                html.H2('Location'),
#d                html.H2('Install Date')
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Here is extract text')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)