from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

IMAGE_SIZE = (500, 500)
THRESHOLD_VALUE = 110
MAX_VALUE = 255
INV_THRESHOLD_VALUE = 50
INV_MAX_VALUE = 255

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/detect', methods=['POST'])
def detect():

    file = request.files['image']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    imageOri = cv2.imread(path)
    image = cv2.cvtColor(imageOri, cv2.COLOR_BGR2GRAY)

    image = cv2.resize(image, IMAGE_SIZE)
    imageOri = cv2.resize(imageOri, IMAGE_SIZE)

    image = cv2.GaussianBlur(image, (3,3),0)

    ret, thresh_basic = cv2.threshold(image, THRESHOLD_VALUE, MAX_VALUE, cv2.THRESH_BINARY)

    kernel = np.ones((5,5),np.uint8)
    img_erosion = cv2.erode(thresh_basic, kernel, iterations=1)

    ret, thresh_inv = cv2.threshold(img_erosion, INV_THRESHOLD_VALUE, INV_MAX_VALUE, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    num_of_con = len(contours) - 1

    for i in range(max(0,num_of_con)):
        cv2.drawContours(imageOri, contours, i, (0,0,255), 1)

    output_path = os.path.join(OUTPUT_FOLDER, file.filename)
    cv2.imwrite(output_path, imageOri)

    return render_template(
        "index.html",
        uploaded=True,
        img=file.filename,
        contours=num_of_con
    )


if __name__ == "__main__":
    app.run(debug=True)