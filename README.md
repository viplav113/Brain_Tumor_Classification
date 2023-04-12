# Brain_Tumor_Classification
This project aims to classify brain tumor images as either having a tumor or not using a deep learning model. The model was built using Keras and trained on a dataset of brain MRI images. The trained model was then integrated into a Flask web application to allow users to upload their own MRI images and receive a prediction on whether or not a brain tumor is present.

The project code includes the following files:

app.py: The main Flask application file that handles image uploads and runs the prediction model.

templates/index.html: The HTML template for the web application's home page.

BrainTomor10Epochs.h5: The pre-trained deep learning model.

static/: A folder containing the CSS and JavaScript files for the web application's front-end.

To run the application, simply clone the repository and run the app.py file. The web application can be accessed at http://localhost:5000.
