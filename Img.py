import numpy as np
from PIL import ImageGrab
from PIL import ImageOps
import cv2


class Img:
    def __init__(self):
        self.screen = self.get_img()


    def gen_img(self):
        raw = ImageGrab.grab(bbox=(1920 / 3 + 60, 2.05 * 1080 / 3, 2 * 1920 / 3 - 70, 1.58 * 1080 / 2))
        w, h = raw.size
        raw = ImageOps.crop(raw, (9, 31, 475, 40))
        raw = raw.resize((200, 300))
        screen = np.array(raw)
        new_screen = self.process_img(screen)
        return new_screen

    def get_img(self):
        return self.screen

    def show_img(self):
        cv2.imshow('window', self.screen)

    def process_img(self, orig_img):
        processed_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
        # processed_img = cv2.Canny(processed_img, threshold1=700, threshold2=100)
        return processed_img
