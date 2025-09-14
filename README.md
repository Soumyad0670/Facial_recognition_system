---

# 🎭 Face Recognition System

A real-time **Face Recognition System** built with [face\_recognition](https://github.com/ageitgey/face_recognition), OpenCV, and Python.
This project lets you **encode faces from images** and then recognize them live using your **webcam**.

---

## 🚀 Features

* Encode multiple faces from images (organized by folders).
* Real-time face detection & recognition from webcam.
* Displays bounding boxes with recognized names.
* Unknown faces are labeled as **"Unknown"**.
* Simple, modular code:

  * `encode_faces.py` → Generate face encodings.
  * `video_stream.py` → Recognize faces in real time.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-system.git
cd face-recognition-system
```

### 2. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install requirements:

```bash
pip install -r dependencies.txt
```

Dependencies include:

* `face_recognition`
* `opencv-python`
* `numpy`

---

## 📂 Project Structure

```
face-recognition-system/
│── known_faces/          # Folder containing subfolders of people’s images
│   ├── Alice/
│   │   ├── alice1.jpg
│   │   └── alice2.jpg
│   └── Bob/
│       ├── bob1.jpg
│       └── bob2.jpg
│
│── encode_faces.py       # Script to encode known faces
│── video_stream.py       # Real-time recognition via webcam
│── utils.py              # Helper to load images
│── encodings.pickle      # Serialized face encodings (generated)
│── dependencies.txt      # Required dependencies
```

---

## 📖 How It Works

### 1. Add Known Faces

* Create a folder `known_faces/`.
* Inside it, make a subfolder for each person (e.g., `Alice/`, `Bob/`).
* Add **multiple clear images** of each person inside their folder.

### 2. Encode Faces

Run the encoding script:

```bash
python encode_faces.py
```

👉 This creates `encodings.pickle` which stores face encodings + labels.

### 3. Start Webcam Recognition

Run:

```bash
python video_stream.py
```

👉 The system opens your webcam and recognizes faces in real time.
👉 Press **`q`** to quit.

---

## 🔍 Behind the Scenes

### `encode_faces.py`

* Loads images from `known_faces/`.
* Extracts face encodings using `face_recognition`.
* Saves encodings + names to `encodings.pickle`.

### `video_stream.py`

* Loads saved encodings.
* Captures video frames via OpenCV.
* Detects faces, compares with known encodings, and displays results.

---

## ⚡ Tips for Better Accuracy

* Use **clear, frontal images** for known faces.
* Add **at least 3–5 images per person** for robustness.
* Ensure good lighting during recognition.

---

## 🛑 Troubleshooting

* **Only "Unknown" shows up?**

  * Check if encodings were created (`encodings.pickle` exists).
  * Make sure images are clear and contain full faces.

* **Webcam not detected?**

  * Ensure it’s working in other apps.
  * Try changing the index in `cv2.VideoCapture(0)` (e.g., `1`).

---

## 🎯 Future Improvements

* Add **face registration via webcam** (no manual folder setup).
* Implement **attendance logging system**.
* Add **GUI interface** for non-technical users.
* Support for **IP camera streaming**.

---

## 📜 License

This project is licensed for **educational purposes only**.
Feel free to fork and modify it for learning and experimentation.

---



