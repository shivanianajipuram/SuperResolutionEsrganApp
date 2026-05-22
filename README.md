# 🚀 AI Image Super-Resolution App (Real-ESRGAN)

This is a deep learning-based Image Super-Resolution system that enhances low-resolution images into high-resolution outputs using Real-ESRGAN (RRDBNet GAN model). It provides a simple Streamlit web interface for easy image upload, processing, and download.

This project demonstrates real-world Computer Vision + Deep Learning inference + Web deployment skills.

---

# 📥 Input

User uploads low-resolution images via Streamlit UI.

Supported formats:
- .png
- .jpg
- .jpeg

Example inputs:
- Blurry images
- Compressed images
- Old / low-quality photos

---

# ⚙️ System Pipeline

Image Upload → Preprocessing → Real-ESRGAN Model → Inference → Upscaling → Output Display → Download

---

# 🧠 Core Technologies

- PyTorch
- Real-ESRGAN (RRDBNet architecture)
- OpenCV
- Pillow (PIL)
- NumPy
- Streamlit

---

# 🔍 How It Works

1. User uploads image via UI
2. Image is converted to RGB format
3. Pretrained Real-ESRGAN model is loaded
4. Deep CNN + GAN enhances image details
5. Image is upscaled (typically 4×)
6. Output is displayed and downloadable

---

# 🤖 Model Used

- RealESRGAN_x4plus.pth (Pretrained GAN model)
- Architecture: RRDBNet (Residual-in-Residual Dense Blocks)
- Type: Super-Resolution GAN

---

# 📁 Project Structure
```bash
SuperResolutionApp/
│
├── app.py
├── inference.py
├── requirements.txt
│
├── weights/
│     └── RealESRGAN_x4plus.pth
│
├── sample_images/
└── README.md
```
---

# 🚀 Local Setup Steps

---

## 1. Clone the repository
```bash
git clone https://github.com/shivanianajipuram/SuperResolutionEsrganApp.git
cd SuperResolutionEsrganApp
```
---

## 2. Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
---

## 3. Install dependencies
```bash
pip install -r requirements.txt
pip install git+https://github.com/xinntao/Real-ESRGAN.git
```
---

## 4. Download model weights

Download:
```bash
RealESRGAN_x4plus.pth
```
From:
```bash
https://github.com/xinntao/Real-ESRGAN/releases
```
Place inside:
```bash
weights/RealESRGAN_x4plus.pth
```
---
## NOTE- copy the whole path which tracks to weights/RealESRGAN_x4plus.pth, paste it in the infernece.py MODEL_PATH variable.
---

## 5. Run application
```bash
streamlit run app.py
```
---

# 🧪 Input to System

- Upload image
- Click "Enhance Image"
- Download high-resolution output

---

# 🔁 Internal Flow

Image → Preprocessing → Feature Extraction → RRDBNet GAN → Upscaling → Output

---

# ⚡ Why This Project Stands Out

- Real Deep Learning GAN model (not simple filters)
- Real-world Computer Vision pipeline
- No API dependency (fully offline inference possible)
- Resume-ready AI project
- Streamlit-based interactive UI
- Deployable on local or cloud (with limitations)

---

# ☁️ Deployment Note (IMPORTANT)
This project uses heavy PyTorch + GAN inference.
You can run Real-ESRGAN locally, but you cannot reliably deploy the pip version on Hugging Face or Render CPU spaces without breaking dependencies.
⚠️ Limitations:
- CPU-based cloud deployment is slow
- First inference takes time (model loading delay)
- GPU is strongly recommended


👉 Best performance:
- Local machine (recommended)
- GPU environments


---



# 💣 Important Note

- You are NOT training the model
- You are using a pretrained GAN model
- Your work = integration + pipeline + UI + deployment

---

# 🧠 Outcome

This project demonstrates:

- Deep Learning inference (GANs)
- Computer Vision preprocessing
- Model loading + inference pipeline
- Web app deployment (Streamlit)
- End-to-end AI system design



#Outputs-
THE STREAMLIT PAGE LOOKS LIKE-
##steps are- 

1.Upload Image
2.After Upload, Click on enhance Image
3.Then Click on Download Image,then It stores Image inside local PC downloads/

<img width="205" height="637" alt="OutputforMeerkat" src="https://github.com/user-attachments/assets/38d7f8aa-2e2a-4670-bd3f-8fcbf02250e4" />


<img width="543" height="620" alt="WhatsApp Image 2026-05-22 at 6 35 08 PM" src="https://github.com/user-attachments/assets/15f69803-d781-4c40-87a3-00f26f0da06a" />


<img width="420" height="512" alt="WhatsApp Image 2026-05-22 at 6 43 12 PM" src="https://github.com/user-attachments/assets/a3861a86-5464-48f9-8ab4-d4fb0ecdac8b" />
