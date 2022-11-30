from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df=pd.read_csv("prop.csv")
 

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",hover_name="name_th",hover_data=['subdistrict_name_th', "size"],
                        color_discrete_sequence=["fuchsia"] , width=1000, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


app.layout = html.Div(children=[
    html.H1(children='Property in Thailand '),

    html.Div(children='''
        this map graph, users can see the density of peoperties in
Thailand..
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
