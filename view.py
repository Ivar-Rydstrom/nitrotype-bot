import numpy as np
from PIL import ImageGrab
from PIL import ImageOps
import cv2
import pytesseract
import pyautogui

screen = np.load('traindata/a.npy')
cv2.imshow('window', screen)
input("hello")
