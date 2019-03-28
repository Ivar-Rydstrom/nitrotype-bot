import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'E:\Ivar\Apps\Tesseract\tesseract.exe'


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=300)
    return processed_img


def get_char(img):
    text = pytesseract.image_to_string(img)
    return text


while(True):
    screen = np.array(ImageGrab.grab(bbox=(1920 / 3 + 60, 2.05 * 1080 / 3, 2 * 1920 / 3 - 70, 1.58 * 1080 / 2)))
    new_screen = process_img(screen)
    detection = get_char(screen)
    if detection:
        char = detection[0]
        pyautogui.keyDown(char)
        pyautogui.keyUp(char)
    print(char)
    # cv2.imshow('window', new_screen)
    cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
