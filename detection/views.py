from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import cv2
import os
import tensorflow as tf
from PIL import Image
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def detection(request):
    """Detects the disease from the image uploaded by the user"""
    if request.method == 'POST':
        try:
            uploadedImage = request.FILES['image']

        except MultiValueDictKeyError:
            return HttpResponse("No image uploaded, please upload an image")

        image = Image.open(uploadedImage)
        image.show()

        image = np.array(image)
        image = cv2.resize(image, (224, 224))
        image = image/255.0

        model = tf.keras.models.load_model('Model/model.h5')

        prediction = model.predict(np.expand_dims(image, axis=0))

        if prediction[0][0] == 1:
            result = "Tumor is detected in the uploaded image."
        else:
            result = "No tumor is detected in the uploaded image."

        return render(request, 'result.html', {result})


def home(request):
    """Renders the home page"""
    return render(request, 'index.html')
