# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

import Map_Creator as mp
import CleaningData as cld
import Graph_Creator as gc
import CSV_Creator as cc
warnings.filterwarnings("ignore")

def main():

    clean19 = cld.data2019Clean(LA19="./data/LACrime_Data_from_2010_to_2019_2.csv")
    clean20 = cld.data2020Clean(LA20="./data/Crime_Data_from_2020_to_Present.csv")

    print(clean19)
    print(clean20)

    hgraph = gc.Histogram(clean19, clean20)
    #pgraph = gc.piePlot(clean19, clean20)

    print(hgraph)
    #print(pgraph)

    map1 = mp.Map(clean19, clean20)
    #map2 = mp.Map(clean20)

    print(map1)
    #print(map2)

if __name__ == "__main__":
    main()

