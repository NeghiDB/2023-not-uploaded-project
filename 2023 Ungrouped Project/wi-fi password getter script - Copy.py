#import os
#import cv2
#import time
#import imutils
#import numpy as np
#from imutils.video import VideoStream
#from tensorflow.keras.models import load_model
#from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input