# body class

from block import Block
from pygame.draw import circle


class Body(Block):
    def __init__(self, x, y):
        super().__init__(x, y, block_type='BODY')
        self.contains_food = False


    def _draw(self, display, radius):
        if not self.contains_food:
            super()._draw(display)
        else:
            super()._draw(display)
            circle(display, (255, 0, 0), (self.x + 25, self.y + 25), radius)


    def _copy(self):
        a = Body(self.x, self.y)
        a.contains_food = self.contains_food
        return a


    def _update(self, body):
        self.x = body.x
        self.y = body.y
        self.contains_food = body.contains_food

