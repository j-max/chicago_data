import geopandas as gpd
from shapely.geometry import Point, Polygon

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as colors


import sys
import os
base_dir = os.getcwd()
repo_name = "chicago_data"
root_path =base_dir.split(repo_name)[0] + repo_name 
sys.path.append(root_path)


def create_geo_df(business_df):
    
    crs = {'init': 'EPSG:4326'}
    geometry = [Point(xy) for xy in zip(business_df['longitude'], business_df['latitude'])]
    geo_df = gpd.GeoDataFrame(business_df, 
                          crs=crs,
                          geometry=geometry)
    
    return geo_df


def create_chicago_map(geo_df, markersize, color=False, title="Businesses in Chicago"):
    shape_file = root_path + "/shape_files/geo_export_13b5a44a-41a4-464a-8d09-00ab1c022c4d.shp"
    chicago_map = gpd.read_file(shape_file)
   
    fig, ax = plt.subplots(figsize = (10,10))
    chicago_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
    if not color:
        geo_df.plot(ax=ax, markersize=markersize)
    else:
        geo_df.plot(ax=ax, column="name", markersize=markersize, categorical=True, cmap='rainbow', legend=True)
    ax.set_title(title)

    return fig, ax