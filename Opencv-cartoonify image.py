import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
import matplotlib.pyplot as plt
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
img = cv2.imread('../input/cartoonify-dataset/girl1.png')
plt.imshow(img )

def displayimg(img1 , cmap=None):
    
    fig= plt.figure(figsize=(12,10))
    ax= fig.add_subplot(111)
    
    plt.xticks([])
    plt.yticks([])
    ax.imshow(img1 , cmap=cmap)
    
#ORIGINAL IMAGE
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
displayimg(img)

#IMAGE PROCESSING
#BLURRING IMAGES TO DENOISE THEM
noiseless_img = cv2.medianBlur( img , 15)

#TURNING IMAGES TO GRAY SCALE
gray_img = cv2.imread('../input/cartoonify-dataset/girl1.png' ,0)

def img_to_gray(img ):
    fig= plt.figure(figsize=(12,10))
    ax= fig.add_subplot(111)
    plt.xticks([])
    plt.yticks([])
    return (ax.imshow(img1 , cmap='gray'))
    
#REMOVE NOISE FROM GRAY SCALE
blur_img = cv2.GaussianBlur( gray_img, (5,5) ,12)
displayimg(blur_img , 'gray')

#APLLY THRESHOLD
def apply_threshold (img):
    
    return cv2.adaptiveThreshold( img , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25,5)
threshold_img = apply_threshold(blur_img)

displayimg(threshold_img, cmap='gray')

#CARTOONIFY COLOURED IMAGE
def cartoonify_filter(image):
    return cv2.bitwise_and(image, image, mask=threshold_img)

cartoonify_img = cartoonify_filter(noiseless_img)

displayimg(cartoonify_img, cmap='gray')


    
