from clarifai.rest import ClarifaiApp
import json
import os
categories = ['cats', 'bulldozers']

app = ClarifaiApp()

model = app.models.get('cats_bulldozers')

for category in categories:
	print category
	for filename in os.listdir('data/'+ category):
		if filename.endswith('.jpg'):
			result = model.predict_by_filename('data/' + category + '/' + filename)
			concepts = result['outputs'][0]['data']['concepts']
			for c in concepts:
				if c['name'] == category:
					print filename, c['value']
