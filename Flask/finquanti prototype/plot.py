import plotly
import plotly.graph_objs as go
#import json
#from pandas.io.json import json_normalize
import pandas as pd
#from datetime import datetime
#import csv
#import os
def genPlot(datafile):
	df = pd.read_json(datafile)
	#print(df)
	candles = df['candles']
	#print(candles)

	complete = []
	volume = []
	time = []
	o = []
	h = []
	l = []
	c = []

	#data = [["complete","volume","time","o","h","l","c"]]
	for i in candles:
		#data = data + [[i["complete"],i["volume"],i["time"],i["mid"]["o"],i["mid"]["h"],i["mid"]["l"],i["mid"]["c"]]]
		complete = complete + [i['complete']]
		volume = volume + [i['volume']]
		time = time + [i['time']]
		o = o + [i['mid']['o']]
		h = h + [i['mid']['h']]
		l = l + [i['mid']['l']]
		c = c + [i['mid']['c']]

	#print(data)

	#with open('data.csv','w') as csvFile:
	#	writer = csv.writer(csvFile)
	#	writer.writerows(data)

	#csvFile.close()

	#datacsv = pd.read_csv('data.csv')
	#datacsv = pd.read_csv(data)

	#os.remove('data.csv')

	trace = go.Candlestick(x=time,
	                open=o,
	                high=h,
	                low=l,
	                close=c)

	data = [trace]
	plotly.offline.plot(data, filename='static/candlestick.html', auto_open=False)
