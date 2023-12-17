from pathlib import Path
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import numpy as np
import cv2
import os
from keras.models import load_model
from PIL import Image
from werkzeug.utils import secure_filename

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
img1 = r"C:\Users\Nidhi Nishad\Desktop\CogniCare\media\no145.jpg"
img2 = r"C:\Users\Nidhi Nishad\Desktop\CogniCare\media\y1.jpg"
# PATH = BASE_DIR / 'media' / 'no145.jpg'


def detection(ig):
    """Detects the disease from the image uploaded by the user"""
    model = load_model("Models/model.h5")
    # imag = Image.open(f'{BASE_DIR / "media" / "no145.jpg"}')

    image = cv2.imread(img2)
    print(image)
    # image.show()
    image = Image.fromarray(image, "RGB")
    image = image.resize((224, 224))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    predict_x = model.predict(input_img)
    print(predict_x)
    return predict_x


def detect(request):
    """Get image from the form and perform operation before prediction."""
    try:
        if request.method == "POST" and request.FILES["file"]:
            uploaded_file = request.FILES["file"]
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.url(filename)

            prediction = detection(file_path)
            # return prediction
            print(prediction)
            if prediction[0][0] < 0.5:
                data = {"result": "Uploaded Image has no Tumor Detected."}
                print(data)
            else:
                data = {"result": "Tumor has been detected in the uploaded image"}
                print(data)
            return render(request, "result.html", {"result": data})
    except Exception as e:
        print(e)
        return HttpResponse("No Image has been uploaded please upload the image.")


def home(request):
    """Renders the home page"""
    return render(request, "index.html")


def catalog(request):
    """Renders the catalog page."""
    return render(request, "catalog.html")


def login(request):
    """User login view."""
    return render(request, "login.html")


def signup(request):
    """User sign up view."""
    return render(request, "signup.html")


def signout(request):
    """User sign out view."""
    pass


# def result(request):
#     if prediction:
#         data = {"result": "Uploaded Image has Tumor Detected."}
#         print(data)
#     else:
#         data = {"result": "No Tumor has been detected in the uploaded image"}
#         print(data)
#     return render(request, "result.html", {"result": data})
