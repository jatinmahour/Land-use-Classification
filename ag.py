import pandas as pd #(version 0.24.2)
import datetime as dt
import dash         #(version 1.0.0)
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bio
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

import plotly       #(version 4.4.1)
import plotly.express as px
import plotly.io as pio
pio.templates.default = "none"

df = pd.read_csv("Classification_of_Area.csv")
# df1=df[df['State'].isin([ 'Bihar',
#        'West Bengal', 'Karnataka', 'Tamil Nadu', 'Punjab'])]
df=df.groupby(['Year','Class_Name','State'],as_index=False).median().reset_index()
BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
app = dash.Dash(__name__,external_stylesheets=[BS])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Classification"),
                dcc.Dropdown(
                    id="class_name",
                    options=[{'label': s, 'value': s} for s in sorted(df.Class_Name.unique())],
        value='Current Fallow',
        clearable=True
                ),
            ]
        ), 
        dbc.FormGroup(
            [
                dbc.Label("States"),
                dcc.Dropdown(
                    id="state_name",
                    options=[],multi=True,
                    clearable=True
                ),
            ]
        )
    ],
     body=True,
        )
app.layout = html.Div([

    html.Div([
        dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Dashboard by Jatin Mahour", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        )
    ],
    color="#2c79fb",
    dark=True,
),

        html.H1("Land Use Classification Of India", style={'font-weight': 'bold',"font-size":"200%",'padding':20,"offset": 4,'color':'#3a3733'}),
        html.Hr(),
        # dbc.Row([
        #     dbc.Col(controls, md=4,style={'color':'#3a3733'}),
        #     dbc.Col(
        html.Div(
    [
        
            dbc.Tabs(
            [
                dbc.Tab(label="Class-Description", tab_id="tab-1"),
                dbc.Tab(label="Pie-Charts", tab_id="tab-2"),
                dbc.Tab(label="Line-Charts", tab_id="tab-3"),
                dbc.Tab(label="Notes", tab_id="tab-4",tab_style={"margin-left": "auto"})
               
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content")
    ]),
    # ]),
    dbc.Row(html.Div(
    [
        dbc.Button(
            "Disclaimer",
            id="simple-toast-toggle",
            color="primary",
            className="mb-3",style={"position": "fixed", "top": 550, "left": 10, "width": 150}
        ),
        dbc.Toast(
            [html.P("The data has been grouped according to states,class and year. The mean value signifies the mean area of all districts of a state for a particular year.  ", className="mb-0")],
            id="simple-toast",
            header="Analysis ",
            icon="primary",
            is_open=False,
            duration=10000,
            dismissable=True,style={"position": "fixed", "top": 500, "left": 10, "width": 500}
        ),
    ]
)


    )
])
])

@app.callback(Output('tabs-content-props', 'children'),
              Input('class_desc', 'value'))

def render_content(tab):
    if tab == 'Forests':
            return html.Div([('Forests: This includes all lands classed as forest under any legal enactment dealing with forests or administered as forests, whether state-owned or private, and whether wooded or maintained as potential forest land. The area of crops raised in the forest and grazing lands or areas open for grazing within the forests should remain included under the forest area.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Area Under Non Agricultural Uses':
        return html.Div([('Area under Non-agricultural Uses: This includes all lands occupied by buildings, roads and railways or under water, e.g. rivers and canals and other lands put to uses other than agriculture.')

            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Barren and Unculturable Land':
        return html.Div([('Barren and Un-culturable Land: includes all barren and unculturable land like mountains, deserts, etc. Land which cannot be brought under cultivation except at an exorbitant cost, should be classed as unculturable whether such land is in isolated blocks or within cultivated holdings.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Permanent Pasture and Other Grazing Land':
        return html.Div([('Permanent Pastures and other Grazing Lands: includes all grazing lands whether they are permanent pastures and meadows or not. Village common grazing land is included under this head.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Land Under Misc. Tree Crops and Groves not Included in Net Area Sown':
        return html.Div([('Land under Miscellaneous Tree Crops, etc. : This includes all cultivable land which is not included in ‘Net area sown’ but is put to some agricultural uses. Lands under Casurina trees, thatching grasses, bamboo bushes and other groves for fuel, etc. which are not included under ‘Orchards’ should be classed under this category.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Culturable Waste Land':
        return html.Div([('Culturable Waste Land: This includes lands available for cultivation, whether not taken up for cultivation or taken up for cultivation once but not cultivated during the current year and the last five years or more in succession for one reason or other. Such lands may be either fallow or covered with shrubs and jungles, which are not put to any use. They may be assessed or unassessed and may lie in isolated blocks or within cultivated holdings. Land once cultivated but not cultivated for five years in succession should also be included in this category at the end of the five years.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Fallow Lands Other Than Current Fallows':
        return html.Div([('Fallow Lands other than Current Fallows: This includes all lands, which were taken up for cultivation but are temporarily out of cultivation for a period of not less than one year and not more than five years.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Current Fallow':
        return html.Div([('Current Fallows: This represents cropped area, which are kept fallow during the current year. For example, if any seeding area is not cropped against the same year it may be treated as current fallow.')
            ],style={"font-size":"120%",'padding':10}),
    if tab == 'Net Area Sown':
        return html.Div([('Net area Sown: This represents the total area sown with crops and orchards. Area sown more than once in the same year is counted only once.')
            ],style={"font-size":"120%",'padding':10})

@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return dbc.Col([
                 dcc.Dropdown(
                    id="class_desc",
                    options=[
                     {'label': 'Forests', 'value': 'Forests'},
                     {'label': 'Area Under Non Agricultural Uses', 'value': 'Area Under Non Agricultural Uses'},
                     {'label': 'Barren and Unculturable Land', 'value': 'Barren and Unculturable Land'},
                     {'label': 'Permanent Pasture and Other Grazing Land', 'value': 'Permanent Pasture and Other Grazing Land'},
                     {'label': 'Land Under Misc. Tree Crops and Groves not Included in Net Area Sown', 'value': 'Land Under Misc. Tree Crops and Groves not Included in Net Area Sown'},
                     {'label': 'Culturable Waste Land', 'value': 'Culturable Waste Land'},
                     {'label': 'Fallow Lands Other Than Current Fallows', 'value': 'Fallow Lands Other Than Current Fallows'},
                     {'label': 'Current Fallow', 'value': 'Current Fallow'},
                     {'label': 'Net Area Sown', 'value': 'Net Area Sown'}
                     ],value='Forests',
            multi=False,
            clearable=False,
            style={"width": "50%"}),
                 html.Div(id='tabs-content-props')
        ],style={'padding':20})
    elif at == "tab-4":
        return html.Div([('The percentage of fallow land has been increasing for most agri-states and net area sown has seen a decline over the years. This clearly indicates that agricultural land is becoming fallow at rate faster than it can replenish itself to regain its fertility')
            ],style={"font-size":"150%",'padding':10})              
    elif at == "tab-3":
        return  dbc.Row([
                dbc.Col(
                controls, md=4,style={'color':'#3a3733','padding':20}
                ),
                dbc.Col(
                dcc.Graph(id='the_graph',figure={}),md=8,style={'color':'#3a3733'}
                     )
                ]),
    elif at == "tab-2":
        return  dbc.Col([
                      dbc.Label("States"),
                dcc.Dropdown(
                    id="state_name_pie",
                    options=[{'label': s, 'value': s} for s in sorted(df.State.unique())]
                     ,value='Madhya Pradesh',
            multi=False,
            clearable=False,
            style={"width": "50%",'padding':5}
                ),
                dcc.Dropdown(
            id='my_dropdown2',
            options=[],
            multi=True,
            clearable=True,
            style={"width": "50%",'padding':5}
                ),
                     dcc.Graph(id='the_pie',figure={})
        ],style={'padding':20})
@app.callback(
    Output('my_dropdown2', 'options'),
    Input('state_name_pie', 'value')
)
def set_states_options(chosen_class):
    dff=df[df.State==chosen_class]
    return [{'label': c, 'value': c} for c in sorted(dff.Year.unique())
    ]
@app.callback(
    Output('my_dropdown2', 'value'),
    Input('my_dropdown2', 'options')
)   
def set_states_value(available_options):
    return [x[0]['value'] for x in available_options
            ] 
@app.callback(
    Output('the_pie', 'figure'),
    Input('state_name_pie', 'value'),
    Input('my_dropdown2', 'value')
)              
def update_grpah(selected_class, selected_state):
    if len(selected_class) == 0:
        return dash.no_update
    else:
        dff = df[(df.State==selected_class) & (df.Year.isin(selected_state))]

        fig = px.pie(
            data_frame=dff,
            values='Area',
            names='Class_Name',
            color='Class_Name',
            color_discrete_map={"Barren and Unculturable Land":"#8b7d56","Forests":"#124800","Area under Non-agricultural Uses":"#dd1942","Permanent Pasture and Other Grazing Land":"#f42e2e","Land Under Misc. Tree Crops and Groves not Included in Net Area Sown":"#2fb303",'Culturable Waste Land':'yellow','Fallow Lands Other Than Current Fallows':'#176188','Current Fallow':'#d04b2b','Net Area Sown':'#077912'},
            hole=.5,
            template='presentation',
           
            )
        return fig

@app.callback(
    Output('state_name', 'options'),
    Input('class_name', 'value')
)
def set_states_options(chosen_class):
    dff=df[df.Class_Name==chosen_class]
    return [{'label': c, 'value': c} for c in sorted(dff.State.unique())
    ]

@app.callback(
    Output('state_name', 'value'),
    Input('state_name', 'options')
)
def set_states_value(available_options):
     return [x[0]['value'] for x in available_options
            ]
@app.callback(
    Output('the_graph', 'figure'),
    Input('class_name', 'value'),
    Input('state_name', 'value')
)
def update_grpah(selected_class, selected_state):
    if len(selected_class) == 0:
        return dash.no_update
    else:
        dff = df[(df.Class_Name==selected_class) & (df.State.isin(selected_state))]

        fig = px.line(dff, x="Year", y="Area",color='State',height=400,log_y=True, width=800,title='Change in mean vaue of area over the years.')
        return fig

@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    return True        

if __name__ == '__main__':
    app.run_server(debug=True)
