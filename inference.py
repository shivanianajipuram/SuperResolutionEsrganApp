import torch
import numpy as np
from PIL import Image
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
import cv2
import os

MODEL_PATH = r"D:\Talentio\Project_10_SuperResolutionApp\Real-ESRGAN\Real-ESRGAN-master\weights\RealESRGAN_x4plus.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define model architecture (IMPORTANT for Real-ESRGAN)
model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=23,
    num_grow_ch=32,
    scale=4
)

upsampler = RealESRGANer(
    scale=4,
    model_path=MODEL_PATH,
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=True if torch.cuda.is_available() else False,
    device=device
)

def enhance_image(pil_img: Image.Image):
    img = np.array(pil_img.convert("RGB"))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    output, _ = upsampler.enhance(img, outscale=4)

    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    return Image.fromarray(output)