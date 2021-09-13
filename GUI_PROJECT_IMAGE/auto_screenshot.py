import time
from PIL import ImageGrab

for i in range(1,11):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)