from clarifai.rest import ClarifaiApp
import os

categories = ['10rp', '1fr', '20rp', '2fr', '50rp']#, 'fr', 'rp']

app = ClarifaiApp()

app.inputs.delete_all()
app.models.delete_all()

for category in categories:
	i = 0
	for filename in os.listdir('data/'+ category):
		if i == 250:
			break
		if filename.endswith('-cropped.png'):
			print filename
			i += 1
			app.inputs.create_image_from_filename('data/' + category + '/' + filename, 
				concepts=[category], not_concepts=[c for c in categories if c != category] )


model = app.models.create(model_id="coins_adsa", concepts=categories)

model.train()
