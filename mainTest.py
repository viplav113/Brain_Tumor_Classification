import cv2
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('BrainTomor10Epochs.h5')

image = cv2.imread('D:\\Brain_Tumor\\pred\\pred0.jpg')

img = Image.fromarray(image)
img = img.resize((64, 64))  # Assign the resized image back to img

img = np.array(img)
input_img = np.expand_dims(img, axis=0)

result = np.argmax(model.predict(input_img), axis=-1)

print(result)
