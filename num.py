import pandas
import json

file = open("allChannels.json",'r')
mydataset = json.load(file)
myvar = pandas.DataFrame(mydataset,index=None)
print(myvar)