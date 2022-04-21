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

def data2019Clean(LA19):
    print("Setting up Dataset 1...")
    #LA19="./data/LACrime_Data_from_2010_to_2019_2.csv"
    headerList = ['DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA', 'AREA NAME', 'Rpt Dist No', 'Part 1-2',
                  'Crm Cd', 'Crm Cd Desc', 'Mocodes', 'Vict Age', 'Vict Sex', 'Vict Descent', 'Premis Cd',
                  'Premis Desc', 'Weapon Used Cd', 'Weapon Desc', 'Status', 'Status Desc', 'Crm Cd 1', 'Crm Cd 2',
                  'Crm Cd 3', 'Crm Cd 4', 'LOCATION', 'Cross Street', 'LAT', 'LON']
    LA19Data = pd.read_csv(LA19, header=None)
    LA19Data.columns = headerList
    LA19DataHead = LA19Data.columns.values.tolist()
    LA19Data = pd.DataFrame(LA19Data)
    #print(LA19Data)
    clean_LA19Data = LA19Data.drop(columns=['DR_NO', 'Date Rptd', 'TIME OCC', 'AREA', 'Rpt Dist No', 'Part 1-2', 'Crm Cd', 'Mocodes', 'Premis Cd',
                 'Premis Desc', 'Weapon Used Cd', 'Weapon Desc', 'Status', 'Status Desc', 'Crm Cd 1', 'Crm Cd 2',
                 'Crm Cd 3', 'Crm Cd 4'])
    Nan_LA19Data = clean_LA19Data.dropna()
    print("Organizing Data to focus on a single Year...")
    Nan_LA19Data[["month", "day", "year"]] = Nan_LA19Data["DATE OCC"].str.split("/", expand=True)
    #Nan_LA19Data = Nan_LA19Data[~(Nan_LA19Data['year'] < '19')]
    #print(Nan_LA19Data['Crm Cd Desc'])
    print("Organizing the Crimes into specific Categories...")
    Nan_LA19Data['category'] = "Other"

    Nan_LA19Data.loc[Nan_LA19Data["Crm Cd Desc"].isin(
        ['THEFT, PERSON', 'VANDALISM - MISDEAMEANOR ($399 OR UNDER)', 'PURSE SNATCHING',
         'THROWING OBJECT AT MOVING VEHICLE', 'THEFT FROM PERSON - ATTEMPT', 'BIKE - ATTEMPTED STOLEN',
         'MOTOR VEHICLE THEFT', 'BURGLARY FROM VEHICLE', 'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)',
         'BURGLARY, ATTEMPTED', 'PURSE SNATCHING - ATTEMPT', 'TILL TAP - GRAND THEFT ($950.01 & OVER)',
         'CRIMINAL DAMAGE', 'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)', 'THROWING OBJECT AT MOVING VEHICLE',
         'THEFT FROM MOTOR VEHICLE - ATTEMPT', 'SHOPLIFTING - ATTEMPT', 'PICKPOCKET, ATTEMPT',
         'CRIMINAL TRESPASS', 'SHOPLIFTING - PETTY THEFT ($950 & UNDER)', 'THEFT OF IDENTITY', 'VEHICLE - STOLEN',
         'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)', 'THEFT, COIN MACHINE - ATTEMPT',
         'BURGLARY', 'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 'ATTEMPTED ROBBERY', 'BUNCO, PETTY THEFT',
         'PICKPOCKET', 'TELEPHONE PROPERTY - DAMAGE', 'DRUGS, TO A MINOR', 'PETTY THEFT - AUTO REPAIR',
         'ROBBERY', 'THEFT PLAIN - PETTY ($950 & UNDER)', 'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD',
         'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)', 'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
         'ARSON', 'BIKE - STOLEN', 'BUNCO, GRAND THEFT', 'BURGLARY FROM VEHICLE, ATTEMPTED', 'VEHICLE - ATTEMPT STOLEN',
         'THEFT PLAIN - ATTEMPT'
         ]), "category"] = "Property"

    Nan_LA19Data.loc[Nan_LA19Data["Crm Cd Desc"].isin(
        ['ASSAULT WITH DEADLY WEAPON', 'KIDNAPPING', 'INTIMATE PARTNER - SIMPLE ASSAULT',
         'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT', 'INTIMATE PARTNER - SIMPLE ASSUALT', 'AGGRAVATED ASSAULT',
         'BATTERY WITH SEXUAL CONTACT', 'BRANDISH WEAPON', 'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
         'SEXUAL PENETRATION W/FOREIGN OBJECT', 'LEWD/LASCIVIOUS ACTS WITH CHILD',
         'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)',
         'BATTERY - SIMPLE ASSAULT', 'INTIMATE PARTNER - SIMPLE ASSUALT', 'CHILD NEGLECT (SEE 300 W.I.C.)',
         'RAPE, ATTEMPTED', 'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH', 'LYNCHING',
         'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM',
         'INTERFERENCE WITH PUBLIC OFFICER', 'CRIMINAL HOMICIDE', 'DISCHARGE FIREARMS/SHOTS FIRED',
         'BATTERY POLICE (SIMPLE)', 'STALKING', 'CRUELTY TO ANIMALS', 'BATTERY ON A FIREFIGHTER', 'FALSE IMPRISONMENT',
         'LYNCHING - ATTEMPTED',
         'RAPE, FORCIBLE', 'INTIMATE PARTNER - AGGRAVATED ASSAULT', 'CRIMINAL THREATS - NO WEAPON DISPLAYED',
         'ORAL COPULATION', 'KIDNAPPING - GRAND ATTEMPT', 'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
         'CHILD ABANDONMENT',
         'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT', 'OTHER ASSAULT',
         'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)', 'SHOTS FIRED AT INHABITED DWELLING',
         'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT'
         ]), "category"] = "Violent"

    Nan_LA19Data.loc[Nan_LA19Data["Crm Cd Desc"].isin(
        ['PUBLIC PEACE VIOLATION', 'RESISTING ARREST', 'SEX,UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ',
         'DISRUPT SCHOOL', 'FAILURE TO DISPERSE',
         'LIQUOR LAW VIOLATION', 'DISTURBING THE PEACE', 'CHILD ANNOYING (17YRS & UNDER)', 'BOMB SCARE', 'DRUNK ROLL',
         'BIGAMY', 'INCITING A RIOT',
         'STALKING', 'OTHER MISCELLANEOUS CRIME', 'RECKLESS DRIVING', 'LEWD CONDUCT', 'WEAPONS POSSESSION/BOMBING',
         'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)',
         'OFFENSE INVOLVING CHILDREN', 'DRIVING WITHOUT OWNER CONSENT (DWOC)', 'THREATENING PHONE CALLS/LETTERS',
         'PEEPING TOM', 'VEHICLE - MOTORIZED SCOOTERS, BICYCLES, AND WHEELCHAIRS',
         'INDECENT EXPOSURE', 'LETTERS, LEWD  -  TELEPHONE CALLS, LEWD', 'FAILURE TO YIELD', 'FALSE POLICE REPORT',
         'PROWLER', 'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)',
         'SEX OFFENSE'
         ]), "category"] = "Public Order"

    Nan_LA19Data.loc[Nan_LA19Data["Crm Cd Desc"].isin(
        ['VIOLATION OF RESTRAINING ORDER', 'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
         'DOCUMENT WORTHLESS ($200 & UNDER)', 'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
         'OBSCENITY', 'DOCUMENT FORGERY / STOLEN FELONY', 'VIOLATION OF TEMPORARY RESTRAINING ORDER', 'BRIBERY',
         'CONSPIRACY', 'CONTRIBUTING',
         'TRESPASSING', 'EXTORTION', 'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE', 'GRAND THEFT / INSURANCE FRAUD',
         'UNAUTHORIZED COMPUTER ACCESS',
         'CONCEALED CARRY LICENSE VIOLATION', 'COUNTERFEIT', 'ILLEGAL DUMPING', 'DISHONEST EMPLOYEE ATTEMPTED THEFT',
         'CREDIT CARDS, FRAUD USE ($950 & UNDER',
         'VIOLATION OF COURT ORDER', 'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
         'DOCUMENT WORTHLESS ($200.01 & OVER)',
         'DECEPTIVE PRACTICE', 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
         'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
         'CONTEMPT OF COURT', 'BUNCO, ATTEMPT'
         ]), "category"] = "White Collar"

    Nan_LA19Data.loc[Nan_LA19Data["Crm Cd Desc"].isin(['RITUALISM', 'PIMPING', 'GRAND THEFT / AUTO REPAIR',
                                                       'OTHER NARCOTIC VIOLATION',
                                                       'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS',
                                                       'CHILD STEALING', 'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE',
                                                       'PROSTITUTION', 'PANDERING',
                                                       'CRIM SEXUAL ASSAULT', 'GAMBLING',
                                                       'CRIMINAL SEXUAL ASSAULT',
                                                       'NARCOTICS'
                                                       ]), "category"] = "Organized"

    clearData = Nan_LA19Data["Crm Cd Desc"][Nan_LA19Data["category"] == "other"].unique()
    #print(Nan_LA19Data)
    if clearData:
        print("Check Again - Not Clear - ERROR!!!")
    else:
        print("Crime Categories have Successfully been sorted...")

    return Nan_LA19Data

#=======================================================================================================================

def data2020Clean(LA20):
    print("Setting up Dataset 2...")
    #LA20="./data/Crime_Data_from_2020_to_Present.csv"
    LA20Data = pd.read_csv(LA20)
    LA20Data = pd.DataFrame(LA20Data)
    clean_LAData = LA20Data.drop(
        columns=['DR_NO', 'Date Rptd', 'TIME OCC', 'AREA', 'Rpt Dist No', 'Part 1-2', 'Crm Cd', 'Mocodes', 'Premis Cd',
                 'Premis Desc', 'Weapon Used Cd', 'Weapon Desc', 'Status', 'Status Desc', 'Crm Cd 1', 'Crm Cd 2',
                 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'])
    clean_LA20Data = clean_LAData.dropna()
    clean_LA20Data['category'] = "Other"

    print("Organizing the Crimes into specific Categories...")
    clean_LA20Data.loc[clean_LA20Data["Crm Cd Desc"].isin(
        ['THEFT, PERSON', 'VANDALISM - MISDEAMEANOR ($399 OR UNDER)', 'PURSE SNATCHING',
         'THROWING OBJECT AT MOVING VEHICLE', 'THEFT FROM PERSON - ATTEMPT', 'BIKE - ATTEMPTED STOLEN',
         'TILL TAP - PETTY ($950 & UNDER)',
         'MOTOR VEHICLE THEFT', 'BURGLARY FROM VEHICLE', 'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)',
         'BURGLARY, ATTEMPTED', 'PURSE SNATCHING - ATTEMPT', 'TILL TAP - GRAND THEFT ($950.01 & OVER)',
         'CRIMINAL DAMAGE', 'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)', 'THROWING OBJECT AT MOVING VEHICLE',
         'THEFT FROM MOTOR VEHICLE - ATTEMPT', 'SHOPLIFTING - ATTEMPT', 'PICKPOCKET, ATTEMPT',
         'CRIMINAL TRESPASS', 'SHOPLIFTING - PETTY THEFT ($950 & UNDER)', 'THEFT OF IDENTITY', 'VEHICLE - STOLEN',
         'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)', 'THEFT, COIN MACHINE - ATTEMPT',
         'BURGLARY', 'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 'ATTEMPTED ROBBERY', 'BUNCO, PETTY THEFT',
         'PICKPOCKET', 'TELEPHONE PROPERTY - DAMAGE', 'DRUGS, TO A MINOR', 'PETTY THEFT - AUTO REPAIR',
         'ROBBERY', 'THEFT PLAIN - PETTY ($950 & UNDER)', 'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD',
         'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)', 'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
         'ARSON', 'BIKE - STOLEN', 'BUNCO, GRAND THEFT', 'BURGLARY FROM VEHICLE, ATTEMPTED', 'VEHICLE - ATTEMPT STOLEN',
         'THEFT PLAIN - ATTEMPT'
         ]), "category"] = "Property"

    clean_LA20Data.loc[clean_LA20Data["Crm Cd Desc"].isin(
        ['ASSAULT WITH DEADLY WEAPON', 'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
         'INTIMATE PARTNER - SIMPLE ASSAULT', 'AGGRAVATED ASSAULT', 'BATTERY WITH SEXUAL CONTACT', 'BRANDISH WEAPON',
         'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER', 'SEXUAL PENETRATION W/FOREIGN OBJECT',
         'LEWD/LASCIVIOUS ACTS WITH CHILD',
         'BATTERY - SIMPLE ASSAULT', 'INTIMATE PARTNER - SIMPLE ASSUALT', 'CHILD NEGLECT (SEE 300 W.I.C.)',
         'RAPE, ATTEMPTED', 'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH', 'LYNCHING',
         'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM', 'KIDNAPPING',
         'INTERFERENCE WITH PUBLIC OFFICER', 'CRIMINAL HOMICIDE', 'DISCHARGE FIREARMS/SHOTS FIRED',
         'BATTERY POLICE (SIMPLE)', 'STALKING', 'CRUELTY TO ANIMALS', 'BATTERY ON A FIREFIGHTER', 'FALSE IMPRISONMENT',
         'LYNCHING - ATTEMPTED', 'INTIMATE PARTNER - SIMPLE ASSUALT',
         'RAPE, FORCIBLE', 'INTIMATE PARTNER - AGGRAVATED ASSAULT', 'CRIMINAL THREATS - NO WEAPON DISPLAYED',
         'ORAL COPULATION', 'KIDNAPPING - GRAND ATTEMPT', 'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
         'CHILD ABANDONMENT', 'MANSLAUGHTER, NEGLIGENT', 'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)',
         'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT', 'OTHER ASSAULT',
         'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)', 'SHOTS FIRED AT INHABITED DWELLING',
         'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT'
         ]), "category"] = "Violent"

    clean_LA20Data.loc[clean_LA20Data["Crm Cd Desc"].isin(
        ['PUBLIC PEACE VIOLATION', 'RESISTING ARREST', 'SEX,UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ',
         'DISRUPT SCHOOL', 'FAILURE TO DISPERSE',
         'LIQUOR LAW VIOLATION', 'DISTURBING THE PEACE', 'CHILD ANNOYING (17YRS & UNDER)', 'BOMB SCARE', 'DRUNK ROLL',
         'INCITING A RIOT', 'BIGAMY', 'FIREARMS RESTRAINING ORDER (FIREARMS RO)',
         'STALKING', 'OTHER MISCELLANEOUS CRIME', 'RECKLESS DRIVING', 'LEWD CONDUCT', 'WEAPONS POSSESSION/BOMBING',
         'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)',
         'OFFENSE INVOLVING CHILDREN', 'DRIVING WITHOUT OWNER CONSENT (DWOC)', 'THREATENING PHONE CALLS/LETTERS',
         'PEEPING TOM', 'VEHICLE - MOTORIZED SCOOTERS, BICYCLES, AND WHEELCHAIRS',
         'INDECENT EXPOSURE', 'LETTERS, LEWD  -  TELEPHONE CALLS, LEWD', 'FAILURE TO YIELD', 'FALSE POLICE REPORT',
         'PROWLER', 'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)',
         'SEX OFFENSE'
         ]), "category"] = "Public Order"

    clean_LA20Data.loc[clean_LA20Data["Crm Cd Desc"].isin(
        ['VIOLATION OF RESTRAINING ORDER', 'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
         'DOCUMENT WORTHLESS ($200 & UNDER)', 'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
         'OBSCENITY', 'DOCUMENT FORGERY / STOLEN FELONY', 'VIOLATION OF TEMPORARY RESTRAINING ORDER', 'BRIBERY',
         'CONSPIRACY', 'CONTRIBUTING', 'DISHONEST EMPLOYEE - PETTY THEFT',
         'TRESPASSING', 'EXTORTION', 'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE', 'GRAND THEFT / INSURANCE FRAUD',
         'UNAUTHORIZED COMPUTER ACCESS',
         'CONCEALED CARRY LICENSE VIOLATION', 'COUNTERFEIT', 'ILLEGAL DUMPING', 'CREDIT CARDS, FRAUD USE ($950 & UNDER',
         'DISHONEST EMPLOYEE - GRAND THEFT',
         'VIOLATION OF COURT ORDER', 'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
         'DOCUMENT WORTHLESS ($200.01 & OVER)', 'CHILD PORNOGRAPHY',
         'DECEPTIVE PRACTICE', 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
         'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
         'CONTEMPT OF COURT', 'BUNCO, ATTEMPT'
         ]), "category"] = "White Collar"

    clean_LA20Data.loc[clean_LA20Data["Crm Cd Desc"].isin(['RITUALISM', 'PIMPING', 'GRAND THEFT / AUTO REPAIR',
                                                           'OTHER NARCOTIC VIOLATION',
                                                           'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS',
                                                           'CHILD STEALING',
                                                           'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE',
                                                           'PROSTITUTION', 'PANDERING',
                                                           'CRIM SEXUAL ASSAULT', 'GAMBLING',
                                                           'CRIMINAL SEXUAL ASSAULT',
                                                           'NARCOTICS'
                                                           ]), "category"] = "Organized"

    clearData = clean_LA20Data["Crm Cd Desc"][clean_LA20Data["category"] == "other"].unique()
    if clearData:
        print("Check Again - Not Clear - ERROR!!!")
    else:
        print("Crime Categories have Successfully been sorted...")

    return clean_LA20Data
