import pandas as pd
import typing
import plotly.express as px
#import numpy as np
from simpledbf import Dbf5
from urllib.request import urlopen
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def file_len(fname):
	with open(fname, encoding="utf-8") as f:
		for i, l in enumerate(f):
			pass
	return i + 1
	
def copyStartFile():
	i = 0
	with open("mv_immeubles_2020t2.csv","r", encoding="utf-8") as f:
		with open("test.csv", "w", encoding="utf-8") as f2:
			for line in f.readlines():
				f2.write(line);
				i += 1;
				if (i > 5000): 
					break


#copyStartFile()

dbf = Dbf5('2020T2_communes.dbf')
#dbf = Dbf5('2020_T2_departement.dbf')

df = dbf.to_dataframe()
#iris = pd.read_csv("mv_immeubles_2020t2.csv")
#iris = pd.read_csv("test.csv")

#https://geo.api.gouv.fr/communes?fields=nom,code&format=json&geometry=centre
with urlopen('file:///I:\devoirsjuju\Esiee1\Python\Python-DataVisualisation/communes-20190101_cut.json') as response:
#with urlopen('file:///C:/Users/vince/OneDrive/Documents/Projet /Python-DataVisualisation/communes-20190101.json') as response:
	counties = json.load(response)


#with urlopen('file:///C:/Users/vince/OneDrive/Documents/Projet/Python-DataVisualisation/communes-20190101.json') as response:
#    counties = json.load(response)



""""fig = px.scatter_mapbox(iris, lat="y", lon="x", 
				color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
				mapbox_style="carto-positron", hover_data=["pm_etat"])"""
"""fig = px.density_mapbox(iris, lat="y", lon="x", 
	color_continuous_scale=px.colors.cyclical.Twilight, zoom=10,
	mapbox_style="carto-positron", hover_data=["pm_etat"], radius=5)"""


fig = px.choropleth_mapbox(df, geojson=counties, locations='INSEE_COM', 
					featureidkey="properties.insee", 
					color='couv', 
					color_continuous_scale="Viridis",
					range_color=(0, 80),
					mapbox_style="carto-positron",
					zoom=4, center = {"lat": 48.853, "lon": 2.3488},
					opacity=0.2,
					labels={'NOM_COM':'nom'})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
	
	
	
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash()
server = app.server
app.layout = html.Div(children=[html.H1(children='TEST'),
								dcc.Graph(
									id='example-graph-1',
									figure=fig
								),
								html.Div(children=
										'''
										Data source from https://www.realestate.com.au/neighbourhoods @Dec 2019
										'''
										)
							])
#page.run_server(debug=True, threaded=True, use_reloader=False)
#fig.show()


if __name__ == "__main__":
	
	app.run_server(debug=True, threaded=True, use_reloader=False)
	
	
	