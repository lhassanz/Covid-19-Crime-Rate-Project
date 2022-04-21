import numpy as np
import os
#import geopandas as gp
import folium
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.mlab as mlab
import pandas as pd
from urllib import request
import scipy as sp
import scipy.stats as st
from scipy import stats as stt
from sklearn import datasets, linear_model
from sklearn.neighbors import KernelDensity as kd
from sklearn.linear_model import LinearRegression
from random import randint
from scipy.stats import norm
import sklearn
import math
import statistics
import sympy as sy
from sympy import symbols, diff
from datetime import date
from scipy.stats import norm, kurtosis
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pylab as py
from scipy.stats import norm, t
from scipy.integrate import quad
import warnings
warnings.filterwarnings("ignore")

def Map(data1, data2):
    Nan_LA19Data1 = pd.read_csv('Updated_LA19_Data.csv')
    clean_LA20Data1 = pd.read_csv('Updated_LA20_Data.csv')

    #gdf = gp.GeoDataFrame(Nan_LA19Data1, geometry=gp.points_from_xy(clean_LA20Data1.LON, Nan_LA19Data1.LAT))
    #gdf = gp.GeoDataFrame(clean_LA20Data1, geometry=gp.points_from_xy(clean_LA20Data1.LON, clean_LA20Data1.LAT))

    map19 = folium.Map(location=[Nan_LA19Data1.LAT.mean(), Nan_LA19Data1.LON.mean()], zoom_start=14,control_scale=True)
    map20 = folium.Map(location=[clean_LA20Data1.LAT.mean(), clean_LA20Data1.LON.mean()], zoom_start=14,control_scale=True)


    for index, location_info in data1.iterrows():
        folium.Marker([location_info["LAT"], location_info["LON"]], popup=location_info["AREA NAME"]).add_to(map19)

    for index, location_info in data2.iterrows():
        folium.Marker([location_info["LAT"], location_info["LON"]], popup=location_info["AREA NAME"]).add_to(map20)

    return map19, map20

