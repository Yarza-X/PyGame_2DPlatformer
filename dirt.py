from sprite import Sprite


class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("sprites/dirt/dirt_texture.png", startx, starty)