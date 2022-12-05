from flask import Flask,render_template,request,url_for
from keras.utils import load_img,img_to_array
from keras.models import load_model
from PIL import Image

import numpy as np


app=Flask(__name__)

disease_class = ['COVID-NEGATIVE','COVID-POSITIVE']

model_path= "model.h5"
model = load_model(model_path)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ['POST','GET'])

def image_load():
    imagefile= request.files['imageflie']
    img_path="static/img/"+imagefile.filename
    imagefile.save(img_path)
    x = load_img(img_path,target_size=(224,224),grayscale = False)
    x = img_to_array(x)
    x = np.expand_dims(x,axis=0)
    pred = model.predict(x)
    a = pred[0]
    temp = np.argmax(a)
    z = disease_class[temp]
    return render_template("index.html",prediction=z)



if __name__=="__main__":
    app.run(debug=True)