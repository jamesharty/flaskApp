import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from myproject import db
from myproject.models import Animal

animals = Animal.query.all()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="",
    brand_href="#",
    sticky="top",
)

body = dbc.Container([

    
    html.H1(children='Animal Data Display'),

    html.Div(children='''
        ID of Animal To Display
    '''),

    dcc.Input(id='input',value='',type='text'),
    html.Div(id='output-graph'),
])


app.layout = html.Div([navbar,body])


def check_siblings(idInput):
    numberOfSiblings =-1

    for x in animals:
        id=x.animalID
        if idInput == id:
            mID=x.motherID
            fID=x.fatherID
            for y in animals:
                if y.motherID == mID or y.fatherID ==fID :
                    numberOfSiblings= numberOfSiblings +1
                
                else:
                    pass
        
            return numberOfSiblings

        else:
            pass
        

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')],
    
)

def update_graph(input_data):
    for x in animals:
        id=x.animalID
        idInput =int(input_data)
        if idInput == id:
            fe =x.feedEfficiency
            mp = x.ch4_daily_mean
            we = x.waterEfficieny
            numberOfSiblings= check_siblings(idInput)
            print(numberOfSiblings)
               
            return dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1], 'y': [we], 'type': 'bar', 'name': 'Water Efficiency'},
                        {'x': [1.5], 'y': [mp], 'type': 'bar', 'name': 'Methane Production'},
                        {'x': [2], 'y': [fe], 'type': 'bar', 'name': 'Feed Efficiency'},
                    ],
                    'layout': {
                        'title':( "Data for animal")
                    }
                }
            )
        else:
            pass

if __name__ == '__main__':
    app.run_server(debug=False)



