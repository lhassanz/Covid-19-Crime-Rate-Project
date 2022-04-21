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

def Histogram(data19, data20):
    #Nan_LA19Data1 = pd.read_csv('Updated_LA19_Data.csv')
    #clean_LA20Data1 = pd.read_csv('Updated_LA20_Data.csv')

    NYear_2019 = data19['category']
    NYear_2020_2021 = data20['category']

    bins = 100

    plt.figure(figsize=(20, 20))
    plt.hist(NYear_2019, bins, alpha=0.5, label='2019', orientation='horizontal')
    plt.hist(NYear_2020_2021, bins, alpha=0.5, label='2020/Early-2021', orientation='horizontal')
    plt.legend(loc='upper right')
    plt.show()

def piePlot(data1, data2):
    mylabels = ["Property", "Violent", "Public Order", "White Collar", "Organized"]

    datalen1 = len(data1['category'])
    datalen2 = len(data2['category'])

    plt.pie(datalen1, labels=mylabels)
    plt.pie(datalen2, labels=mylabels)

    plt.show()