import pandas
import json

file = open("allChannels.json",'r')
mydataset = json.load(file)
myvar = pandas.Series(mydataset)
print(myvar[0])