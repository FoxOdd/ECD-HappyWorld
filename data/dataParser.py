#!/usr/bin/env python3

"""Simple script to make csv with us datas"""

__author__ = ["Odd", "Maud"]
__copyright__ = "2021, Lyokô Corp"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "odd.heurtel@gmail.com"
__status__ = "Developpement"

import os
import pandas
import re
import json

LIST_EXT = ["csv", "json"]  # Extension’s list of interests
BLACK_LIST = ['Indicators.csv', 'ISO3166.csv']
HEADER_Skip = ['ISO', 'FR_Country', 'EN_country', 'ES_country', 'AR_country', 'FA_country', 'Zone']
YEARS = [2013, 2014, 2014, 2015, 2016, 2017, 2018, 2019, 2020]


class Fichier():
    def __init__(self, path, name, year):
        self.path = path
        self.name = name
        self.header = []
        self.DF = None
        self.json = None
        self.year = int(year)

    def __repr__(self):
        try:
            if self.DF is not None:
                return f"{self.path} year {self.year} have {self.DF.shape} dimensions and {len(self.header)} variables\n"
            if self.json is not None:
                return f"{self.path} year {self.year} have {len(self.json)} keys and {len(self.header)} variables\n"
            else:
                return f"{self.path} year {self.year} have unknow dimensions and {len(self.header)} variables\n"
        except AttributeError:
            return f"{self.path} year {self.year} have {len(self.header)} variables\n"

    def getValues(self, method):
        """
        To apply pandas read.

        method for pandas csv or json
        """
        print(f"Parsing with panads : {os.path.join(self.path, self.name)} with method {method}")
        if method == 'csv':
            self.DF = pandas.read_csv(os.path.join(self.path, self.name))
            self.header = list(self.DF.columns)
        if method == 'json':
            # self.DF = pandas.read_json(os.path.join(self.path, self.name))
            # self.header = list(self.DF.columns)
            self.json = json.load(open(os.path.join(self.path, self.name), 'r'))


extension = lambda name: name.rstrip().split('.')[-1]


ECD = {}
ISO3166 = pandas.read_csv('ISO3166.csv')

print("INFO: parsing Start")
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        extensionFile = extension(name)
        if extensionFile in LIST_EXT and name not in BLACK_LIST:
            y = re.search('\d{4}', name)
            try:
                year = y.group(0)
            except AttributeError as e:
                year = 0
            ECD[name] = Fichier(root, name, year)
            ECD[name].getValues(extensionFile)

print("INFO: export of all datas")

index = ISO3166.iloc[:, 0].values.tolist()

# make header
columnsExport = {}
for nameFile in ECD:
    """
    if ECD[nameFile].year == yearInterest and extension(ECD[nameFile].name) == 'csv':
        for header in ECD[nameFile].header:
            if header in columnsExport:
                print("WARNING : header already in columnsExport list")
                continue  # to evit overwrite data
            if header not in columnsExport and header not in HEADER_Skip:
                columnsExport[header] = []
    """
    # traitement json file
    if extension(ECD[nameFile].name) == 'json':
        dataBufferDict = {}
        if type(ECD[nameFile].json) is dict:
            # columns for pandas
            keyIndicator = list(ECD[nameFile].json['indicator_name'].keys())[0]
            valueKeyIndicator = ECD[nameFile].json['indicator_name'][keyIndicator]
            if keyIndicator not in columnsExport:
                columnsExport[keyIndicator] = valueKeyIndicator

# fill dataframe
for yearInterest in YEARS:
    print(f"INFO: {yearInterest} : ", end='')
    # make data frame pandas empty
    dataExport = pandas.DataFrame(columns=list(columnsExport.values()), index=index)
    dataExport = dataExport.loc[~dataExport.index.duplicated(), ~dataExport.columns.duplicated()]
    for nameFile in ECD:
        if extension(ECD[nameFile].name) == 'json':
            if type(ECD[nameFile].json) is dict:
                # print(f"start : {ECD[nameFile].name}")
                keyIndicator = list(ECD[nameFile].json['indicator_name'].keys())[0]
                valueKeyIndicator = ECD[nameFile].json['indicator_name'][keyIndicator]
                # country, indicator_value, year, value
                for country in ECD[nameFile].json['indicator_value'].keys():
                    for iv in ECD[nameFile].json['indicator_value'][country].keys():
                        if iv == keyIndicator:
                            for year in ECD[nameFile].json['indicator_value'][country][iv].keys():
                                if int(year) == yearInterest:
                                    # get value
                                    dataExport.at[country, valueKeyIndicator] = ECD[nameFile].json['indicator_value'][country][iv][year]
                # print(f"end : {ECD[nameFile].name}")
    dataExport.to_csv(f"export/{yearInterest}.csv", na_rep='NA')
    print(f"exported")
