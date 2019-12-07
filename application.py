# import the necessary packages
import base64
from keras.models import load_model
import keras
from flask import request, render_template, jsonify
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import imagenet_utils
from keras import backend as K
from PIL import Image
import numpy as np
import flask
import io

# initialize our Flask application and the Keras model
application = flask.Flask(__name__)
model = None

def load_nmodel():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    global model
    model = load_model('xray_model.h5')

def prepare_image(image, target_size):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # return the processed image
    return image
    
@application.route("/")
def home():
    return render_template('index.html')


@application.route("/predict", methods=["POST"])
def predict():

    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = prepare_image(image, target_size=(224,224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction':{
            'Normal': prediction[0][0],
            'Pneumonia': prediction[0][1]
        }
    }

    # return the data dictionary as a JSON response
    return flask.jsonify(response)

# command to curl 
# curl -X POST -F image=@dog.jpg "http://localhost:5000/predict"

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_nmodel()
    application.run(debug= False, threaded = False)