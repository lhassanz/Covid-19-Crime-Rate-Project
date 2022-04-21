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

#Didn't have enough time to fix this it was considered last priority for the project
"""
def createCSV(dataset1, dataset2):
    dataset1 = "Updated_LA19_Data.csv"
    Nan_LA19Data.to_csv(file_name2)
    #Nan_LA19Data.to_csv(r'', index=False)

    dataset2 = "Updated_LA20_Data.csv"
    clean_LA20Data.to_csv(file_name2)
    #clean_LA20Data.to_csv(r'', index=False)

    return 

    completeName = os.path.join(save_path, file_name)
    #print(completeName)
#"""