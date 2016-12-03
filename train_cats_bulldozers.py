from clarifai.rest import ClarifaiApp
import os

categories = ['cats', 'bulldozers']

app = ClarifaiApp()

app.inputs.delete_all()
app.models.delete_all()

for category in categories:
	for filename in os.listdir('data/'+ category):
		if filename.endswith('.jpg'):
			print filename
			app.inputs.create_image_from_filename('data/' + category + '/' + filename, 
				concepts=[category], not_concepts=[c for c in categories if c != category] )


model = app.models.create(model_id="cats_bulldozers", concepts=categories)

model.train()
