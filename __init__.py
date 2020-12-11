import typing # Enable static variable annotations
from simpledbf import Dbf5 # Used to extract data from .dbf files
import os
dirname = os.path.dirname(__file__)

# DataScience and display libs
from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def file_len(fname):
	"""Get the file len. Was usefull for tests on big documents

	Args:
		fname (string): path of the file

	Returns:
		int: number of lines
	"""
	with open(fname, encoding="utf-8") as f:
		for i, l in enumerate(f):
			pass
	return i + 1


def main():
		
	# Read and convert the Dbf5 format into a usable dataframe format
	dbf = Dbf5("data/2020T2_communes.dbf")
	df = dbf.to_dataframe() 

	# Read a geojson file used in the map
	with urlopen("file:" + os.path.join(dirname, "data/communes-20190101.json")) as response:
		counties = json.load(response)


	# Debug help
	for col in df.columns:
		print(col, end=" ")
	print("")

	# Create a map on the fiber cover
	fig = px.choropleth_mapbox(
		df,
		geojson=counties,
		locations="INSEE_COM",
		featureidkey="properties.insee", # super important - This is the path to the geojson field that match with INSEE_COM
		color="couv", # the color will depends of couv
		color_continuous_scale="BuPu",
		range_color=(0, 80),
		mapbox_style="carto-positron",
		zoom=4,
		center={"lat": 48.853, "lon": 2.3488}, # Center on Paris
		opacity=0.5,
		hover_data=["NOM_COM"], # Add the city name on mouse hover
		labels={"NOM_COM": "Commune ", "couv": "Couverture de fibre "}, # Rename the labels
	)
	fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


	# Select only 2 columns and group cities by couv
	df2 = df[["couv", "NOM_COM"]].groupby("couv").count().reset_index()
	print(df2)
	fig2 = px.histogram(df2, x="couv", y="NOM_COM", log_y=True, labels=dict(couv= "Couverture de fibre"))
	fig2.update_layout(bargap=0.1, yaxis_title="Total de communes")
	fig2.update_traces(xbins=dict( 
			start=0,
			end=90,
			size=10
		))


	# Use dash and create the html template
	app = dash.Dash()
	server = app.server
	app.layout = html.Div(
		children=[
			html.H1(children="Où en est le déploiment de la fibre en France ?"),
			html.Div(
				children=[
					dcc.Graph(id="example-graph-1", figure=fig, style = {"width": "100%"}),
					dcc.Graph(id="example-graph-2", figure=fig2, style = {"width": "100%"}),
				],
				style =	{"display": "flex", "flex-direction": "row", "width": "95%"}
			),
			html.Div(
				children=["Source DataGouv ",
					html.A("link", href="https://www.data.gouv.fr/fr/datasets/le-marche-du-haut-et-tres-haut-debit-fixe-deploiements/")
				]
			),
		]
	)
	app.run_server(debug=True, threaded=True, use_reloader=False)


if __name__ == "__main__":
	main()
