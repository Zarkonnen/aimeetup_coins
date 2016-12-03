from clarifai.rest import ClarifaiApp
import json
import os
categories = ['10rp', '1fr', '20rp', '2fr', '50rp']#, 'fr', 'rp']

app = ClarifaiApp()

model = app.models.get('coins_adsa')

tests = 0
correct = 0

for category in categories:
	print category
	for filename in os.listdir('data/'+ category):
		if filename.endswith('-cropped.png'):
			result = model.predict_by_filename('data/' + category + '/' + filename)
			concepts = result['outputs'][0]['data']['concepts']
			tests += 1
			if concepts[0]['name'] == category:
			    correct += 1
			for c in concepts:
				if c['name'] == category:
					print filename, c['value'], concepts[0]['name'], concepts[0]['value']

print str(correct * 100 / tests), "% accuracy"
