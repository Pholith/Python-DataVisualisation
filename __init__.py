import pandas as pd
import typing
import plotly.express as px
#import numpy as np
from simpledbf import Dbf5
from urllib.request import urlopen
import json

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

def main():
    #copyStartFile()

    dbf = Dbf5('2020T2_communes.dbf')
    df = dbf.to_dataframe()
    #iris = pd.read_csv("mv_immeubles_2020t2.csv")
    #iris = pd.read_csv("test.csv")

    with urlopen('https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre') as response:
        counties = json.load(response)
        for element in counties:
            element["INSEE_COM"] = element["code"]
            
    

      
    
    """"fig = px.scatter_mapbox(iris, lat="y", lon="x", 
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                    mapbox_style="carto-positron", hover_data=["pm_etat"])"""

    """fig = px.density_mapbox(iris, lat="y", lon="x", 
        color_continuous_scale=px.colors.cyclical.Twilight, zoom=10,
        mapbox_style="carto-positron", hover_data=["pm_etat"], radius=5)"""


    fig = px.choropleth_mapbox(df, geojson=counties, locations='INSEE_COM', color='couv',
                        color_continuous_scale="Viridis",
                        range_color=(0, 100),
                        mapbox_style="carto-positron",
                        zoom=3, center = {"lat": 48.853, "lon": 2.3488},
                        opacity=0.5,
                        labels={'unemp':'unemployment rate'}
                        )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    fig.show()


if __name__ == "__main__":
    main()
    
    
        