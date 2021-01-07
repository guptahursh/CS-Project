#-------------- IMPORTS ---------------#
import ctypes
import json
with open('settings.json','r') as f:
    data = json.load(f)

class Settings:
    def __init__(self):
        self.width = data["width"]
        self.height = data["height"]
        self.fps = data["fps"]
        self.playerWidth = data["playerWidth"]
        self.playerHeight = data["playerHeight"]
        self.gravity = data["gravity"]
        self.block_size = data["block_size"]
        self.colors = data["colors"]
        self.base_acc = data["base_acc"]

    def getDisplaySize(self):
        try:
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            return screensize
        except:
            return (1280,720)

LB_x = LB_y = 0 - data['bounds']
UB_x = data['bounds'] + data['width']
UB_y = data['bounds'] + data['height']
