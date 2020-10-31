import pandas as pd
from Rappers import Rappers
import reverse_geocoder as rg

class Data :
    def __init__(self,fileCSV,sep):
        self.file = fileCSV
        self.data = pd.read_csv(fileCSV,sep=sep)
        self.listCountry = list()
        self.listName = list()
    

    def getData(self):
        return self.data
    
    def statistique(self):
        print(self.data.describe())

    def readColumn(self):
        print(self.data.columns)
    
    def getColumn(self,column):
        print(self.data[column])
        return self.data[column]
    
    def reverseLatLng(self,latlng):
        coor = (latlng[0],latlng[1])
        geo = rg.search(coor)
        country = geo[0]['cc']
        return country

    
    def getRapper(self,column="Name"):
        #print(self.data[column])
        listName = list()
        for tupl in self.data[column] :
            listName.append(tupl)
        self.listName = listName
        return self.listName
        

    def getCountry(self,column="Coordinates"):
        #print(self.data[column])
        listLatLng = list()
        for tupl in self.data[column] :
            latlng = tupl.split(",")
            listLatLng.append(latlng)
            country = self.reverseLatLng(latlng)
            self.listCountry.append(country)
        return self.listCountry
    

df = pd.read_csv("countryRapper.csv",sep=",")
"""
fr = (df["Country"] == 'FR')
n = (df["Name"].notnull())
dfr = df[fr & n]
print(dfr.count())
"""
dfC = df.groupby("Country")

print(dfC.head(5))

