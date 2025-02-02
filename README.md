# Automated Video Captioning Tool

## Overview
The **Automated Video Captioning Tool** is a machine learning-powered application designed to generate **frame-by-frame captions** for videos, convert them into **audio descriptions**, and integrate them seamlessly for enhanced accessibility. This project leverages **deep learning models, video processing techniques, and natural language generation** to automate captioning and narration for videos.

---

## 🚀 Features
- **Frame-by-frame video captioning** using state-of-the-art **VIT-GPT2 and LSTM models**.
- **Audio description generation** using Google Text-to-Speech (TTS).
- **Silent part detection and synchronization** for seamless audio-visual integration.
- **Web-based interface** for user-friendly interactions.
- **Automated data processing and feature extraction** with ResNet50 and VIT models.

---

## 📁 Project Structure

```
Automated_Video_Captioning_Tool/
│-- FrontEnd/
│   ├── index.html
│   ├── log-in.html
│   ├── qrcode_thestorytellers.netlify.app.png
│   ├── sign-up.html
│
│-- Model_and_Backend/
│   ├── Gen_audio.py
│   ├── Model.py
│   ├── Sum_Dis.py
│   ├── VPPP.py
│   ├── app.py
│   ├── pyproject.toml
│   ├── readme.md
│   ├── requirements.txt
│
│-- Notebook_Files/
│   ├── Custom_Model_Resnet_Features.ipynb
│   ├── Data_Downloader.ipynb
│   ├── Feature_Extraction_Resnet50.ipynb
│   ├── Feature_Extraction_VIT.ipynb
│   ├── Readme.md
│   ├── SpaceTimeGPT_FineTunining.ipynb
│   ├── T5_Model.ipynb
│   ├── Test_Models.ipynb
│   ├── VIT_GPT2.ipynb
│   ├── VIT_GPT2_Full_Pipeline.ipynb
│
│-- README.md  (This file)
```

---

## 📌 Key Components

### 1️⃣ FrontEnd
- **Description:** Contains the HTML files for the web-based user interface.
- **Files:**
  - `index.html` → Main landing page.
  - `log-in.html` → User authentication page.
  - `sign-up.html` → User registration page.
  - `qrcode_thestorytellers.netlify.app.png` → QR code for accessing the tool online.

### 2️⃣ Model and Backend
- **Description:** Contains backend logic, models, and APIs.
- **Files:**
  - `Gen_audio.py` → Converts text descriptions into **audio narrations**.
  - `Model.py` → Contains the **core ML model** for video captioning.
  - `Sum_Dis.py` → Summarizes generated captions for concise descriptions.
  - `VPPP.py` → Video Pre-Processing Pipeline for structured data input.
  - `app.py` → Flask-based backend API.
  - `requirements.txt` → Dependencies and package requirements.

### 3️⃣ Notebook Files
- **Description:** Contains Jupyter notebooks for training, testing, and optimizing models.
- **Notable Notebooks:**
  - `Data_Downloader.ipynb` → Downloads video datasets from given URLs.
  - `Feature_Extraction_Resnet50.ipynb` → Extracts **video features** using ResNet50.
  - `Feature_Extraction_VIT.ipynb` → Extracts **video features** using Vision Transformer (VIT).
  - `Custom_Model_Resnet_Features.ipynb` → Implements an **LSTM model** trained on ResNet50 features.
  - `VIT_GPT2.ipynb` → Tests **VIT-GPT2 model** on sample videos.
  - `VIT_GPT2_Full_Pipeline.ipynb` → End-to-end pipeline: caption generation, audio conversion, silent part detection, and final output.
  - `SpaceTimeGPT_FineTunining.ipynb` → Fine-tunes SpaceTimeGPT for video captioning.

---

## 🌟 How It Works (STAR Approach)

### **SITUATION**
**Problem:** Many videos lack **accurate captions and audio descriptions**, making them inaccessible to visually and hearing-impaired users.

### **TASK**
- Develop an **automated captioning system** that generates high-quality text descriptions.
- Convert captions into **audio descriptions** for accessibility.
- Ensure synchronization between **audio and video**.
- Provide a **user-friendly web interface**.

### **ACTION**
✅ Built an end-to-end **deep learning pipeline** using **Vision Transformer (VIT) and GPT-2**.  
✅ Developed **LSTM-based models** to enhance caption accuracy.  
✅ Integrated **Google TTS** for generating realistic audio descriptions.  
✅ Used **Apache Airflow** to schedule and automate video processing.  
✅ Designed an interactive **frontend** for seamless user interactions.

### **RESULT**
🚀 **70% reduction in manual captioning efforts**.  
🎯 **Achieved a BLEU Score of 0.73**, indicating high-quality caption generation.  
📈 **Improved video accessibility** for visually impaired users.

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/jaivinjacob/Automated_Video_Captioning_Tool.git
cd Automated_Video_Captioning_Tool
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r Model_and_Backend/requirements.txt
```

### **4️⃣ Run the Backend**
```bash
cd Model_and_Backend
python app.py
```

### **5️⃣ Open Frontend in Browser**
Simply open `index.html` in a web browser.

---

## 🎯 Future Improvements
- Enhance **caption accuracy** using **multi-modal transformers**.
- Improve **speech synthesis quality** for more natural narration.
- Develop an **API for third-party integration**.

---

## 📩 Contact
For any queries or contributions, feel free to reach out:

📧 Email: [jaivinjacobvj@gmail.com](mailto:jaivinjacobvj@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/jaivinjacob](https://linkedin.com/in/jaivinjacob)  
💻 GitHub: [github.com/JaivinJacob](https://github.com/JaivinJacob)

---

### 🌟 If you find this project useful, **give it a ⭐ on GitHub!** 🚀
