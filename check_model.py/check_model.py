from tensorflow.keras.models import load_model

# Load your model
model = load_model('model/waste_classifier.h5')

# Print summary of the model
model.summary()
