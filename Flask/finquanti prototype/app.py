from flask import Flask,render_template,request,url_for,redirect
from werkzeug import secure_filename
import os
import plot

#app = Flask(__name__)

#plot.genPlot('data.json')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route("/charts")
def charts(page='charts'):
	return render_template('charts.html',page=page)

@app.route("/showplot")
def showplot(page='showplot'):
	return render_template('charts.html',page='showplot')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():   
	if 'data' in request.files:
		data = request.files['data']
		if data.filename != '':
			plot.genPlot(data)
	return redirect(url_for('showplot'))


if __name__ == '__main__':
	app.run(debug = True)