from functions import *
from settings import *


class Button:
    def __init__(self, gl, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.gl = gl
        self.event = None

        self.button = gl.gui.GUI_TEXTURES["button_bg"]

    def setEvent(self, event):
        self.event = event

    def update(self, mp, mc):
        self.button = self.gl.gui.GUI_TEXTURES["button_bg"]

        if checkHover(self.x, self.y,
                      self.button.width, self.button.height,
                      mp[0], mp[1]):
            self.button = self.gl.gui.GUI_TEXTURES["button_bg_hover"]
            if mc == 1:
                pass
                self.gl.sound.playGuiSound("click")
                if self.event:
                    self.event()

        self.button.blit(self.x, HEIGHT - self.y - self.button.height)
        drawInfoLabel(self.text, xx=WIDTH // 2, yy=HEIGHT - self.y - 25, style=[('', '')],
                      size=12, anchor_x='center')