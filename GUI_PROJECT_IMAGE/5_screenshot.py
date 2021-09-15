import keyboard
import datetime
from PIL import ImageGrab

def screenshot():
    now = datetime.datetime.now()
    img = ImageGrab.grab()
    img.save("image{}.png".format(1))

keyboard.add_hotkey("F9",screenshot)    # F9 를 누르면 스크린 샷 저장

keyboard.wait("esc")    # esc를 누를 때 까지 프로그램 수행