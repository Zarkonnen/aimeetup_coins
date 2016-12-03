from clarifai.rest import ClarifaiApp
import os

categories = ['10rp', '1fr', '20rp', '2fr', '50rp', 'fr', 'rp']

app = ClarifaiApp('HfNL8Isbamm0_iTsJ4taYh8AcBrVflvzwbAj12it', 'yPJzQrJ6q0fMnde940BBzz9SMmrt1dbbZMRL4lv8')

app.inputs.delete_all()
app.models.delete_all()

for category in categories:
	for filename in os.listdir('data/'+ category):
		if filename.endswith('.png'):
			print filename
			app.inputs.create_image_from_filename('data/' + category + '/' + filename, 
				concepts=[category], not_concepts=[c for c in categories if c != category] )


model = app.models.create(model_id="coins_adsa", concepts=categories)

model.train()