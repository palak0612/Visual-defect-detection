# 🧠 Image Defect Detection Web App (OpenCV + Flask)

A Computer Vision based web application that detects **defects in images using OpenCV image processing techniques**.
Users can upload an image through a web interface, and the system automatically processes the image to **detect and highlight defects using contour detection**.

This project demonstrates the use of **Python, OpenCV, Flask, and basic frontend development** to build a practical image inspection tool.

# 🚀 Features

* Upload images through a web interface
* Detect defects using OpenCV image processing
* Highlight detected defects with contour outlines
* Display the number of detected defects
* Simple and user-friendly interface
* Fast processing using optimized image operations

# 🛠️ Technologies Used

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Python     | Core programming language             |
| Flask      | Backend web framework                 |
| OpenCV     | Image processing and defect detection |
| NumPy      | Numerical operations                  |
| HTML       | Frontend interface                    |
| CSS        | Basic styling                         |

# 📂 Project Structure

```
Image-Defect-Detection
│
├── app.py
│
├── templates
│   └── index.html
│
├── static
│   ├── uploads
│   └── output
│
└── README.md
```

# ⚙️ How the System Works

The defect detection process follows several image processing steps:

### 1️⃣ Image Upload

The user uploads an image through the web interface.

### 2️⃣ Image Preprocessing

* Convert image to **grayscale**
* Resize image for consistent processing
* Apply **Gaussian Blur** to remove noise

### 3️⃣ Thresholding

Binary thresholding is applied to separate the object from the background.

### 4️⃣ Morphological Processing

Erosion is used to remove unwanted small noise.

### 5️⃣ Inverse Threshold

Used to isolate potential defect areas.

### 6️⃣ Contour Detection

OpenCV identifies contours representing defects in the image.

### 7️⃣ Defect Highlighting

Contours are drawn on the original image to highlight defect regions.

# 📸 Example Output

**Input:** Uploaded image
**Output:** Image with red contour marks indicating detected defects.

The system also displays:

```
Contours Detected: X
```

Where **X** represents the number of detected defects.

# 🧑‍💻 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/image-defect-detection.git
cd image-defect-detection
```

### 2️⃣ Install Dependencies

```
pip install flask opencv-python numpy
```

# ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

Upload an image to detect defects.

# 📌 Future Improvements

* Deep learning based defect detection
* Improved UI using React or Bootstrap
* Support for multiple image uploads
* Real-time camera defect detection
* Cloud deployment (AWS / Render / Heroku)

# 🎯 Applications

* Manufacturing quality inspection
* Product surface defect detection
* Industrial automation
* Machine vision systems

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

# 📜 License

This project is open-source and available under the **MIT License**.


# 👩‍💻 Author

**Palak**

⭐ If you like this project, consider giving it a **star on GitHub!**
