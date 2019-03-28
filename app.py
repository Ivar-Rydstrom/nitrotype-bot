import numpy as np
from PIL import ImageGrab
from PIL import ImageOps
import cv2
import pytesseract
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'E:\Ivar\Apps\Tesseract\tesseract.exe'


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=700, threshold2=100)
    return processed_img


def get_char(img):
    text = pytesseract.image_to_string(img)
    return text


while(True):
    raw = ImageGrab.grab(bbox=(1920 / 3 + 60, 2.05 * 1080 / 3, 2 * 1920 / 3 - 70, 1.58 * 1080 / 2))
    w, h = raw.size
    # raw = ImageOps.crop(raw, (11, 31, 477, 40))
    # raw = raw.resize((200, 300))
    screen = np.array(raw)
    new_screen = process_img(screen)
    # new_screen = screen
    detection = get_char(new_screen)
    if detection:
        char = detection[0]
        pyautogui.keyDown(char)
        pyautogui.keyUp(char)
        print(char)
    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
