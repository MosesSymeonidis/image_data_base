import math
import numpy as np
import skimage
from skimage.feature import local_binary_pattern
from skimage.util import img_as_ubyte
import cv2

def histogram(afile):

    nparr = np.fromstring(afile.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
    #print(np.max(img))
    #
    #---------------------------------------------------------------------------
    n=7
    histogram_texture=[0]*(n**3)
    histogram_color=[0]*(n**3)
    height, width, depth = img.shape
    pix=480000
    x=int(round(math.sqrt(pix*height/width)))
    y=int(round(math.sqrt(pix*width/height)))
   # print(2)
    img = skimage.transform.resize(img, (x,y))
    x1,y1,h=img.shape

    #print(2)
    img=img_as_ubyte(img)
   # print(np.max(img))
    #----------------------------------------------------------------------------
    indices = np.arange(0,256)   # List of all colors
    divider = np.linspace(0,255,n+1)[1] # we get a divider
    quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
    #print(quantiz)
    color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
    palette = color_levels # Creating the palette
    color_matrix = palette[img]  # Applying palette on image
    #----------------------------------------------------------------------------
   # print(np.max(color_matrix))
    gray = skimage.color.rgb2gray(img)

    lbp = local_binary_pattern(gray, n, 4, "default")
    lbp=lbp.astype(int)

    for i in range(x1):
        for j in range(y1):
             histogram_color[((n ** 2) * color_matrix[i,j,0]) + (n*color_matrix[i,j,1]) + color_matrix[i,j,2]]+= 1
             histogram_texture[lbp[i,j]]+=1
    #print(histogram_color)
    return histogram_color,histogram_texture