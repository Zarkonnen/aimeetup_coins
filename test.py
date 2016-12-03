from clarifai.rest import ClarifaiApp
import json
import os
categories = ['10rp', '1fr', '20rp', '2fr', '50rp', 'fr', 'rp']

app = ClarifaiApp()

model = app.models.get('coins_adsa')

for category in categories:
	print category
	for filename in os.listdir('data/'+ category):
		if filename.endswith('.png'):
			result = model.predict_by_filename('data/' + category + '/' + filename)
			#result = json.loads(result_json)
			concepts = result['outputs'][0]['data']['concepts']
			for c in concepts:
				if c['name'] == category:
					print filename, c['value']