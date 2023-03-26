# Head class

from block import Block
from body import Body

class Head(Block):
    def __init__(self, x, y):
        super().__init__(x, y, block_type='HEAD')
        self.dir = 'UP'
        self.contains_food = False


    def _check_bound(self, window_size, size):
        if self.x == -size:
            self.x += window_size[0]
        elif self.x == window_size[0]:
            self.x = 0
        elif self.y == -size:
            self.y += window_size[1]
        elif self.y == window_size[1]:
            self.y = 0
        else:
            pass


    def _update(self, action, food, window_size, size):
        def update():
            if self.dir == 'UP':
                self.y -= self.size
            elif self.dir == 'DOWN':
                self.y += self.size
            elif self.dir == 'LEFT':
                self.x -= self.size
            else:
                self.x += self.size

        def left():
            if self.dir == 'UP':
                self.dir = 'LEFT'
            elif self.dir == 'DOWN':
                self.dir = 'RIGHT'
            elif self.dir == 'LEFT':
                self.dir = 'DOWN'
            else:
                self.dir = 'UP'

        def right():
            if self.dir == 'UP':
                self.dir = 'RIGHT'
            elif self.dir == 'RIGHT':
                self.dir = 'DOWN'
            elif self.dir == 'DOWN':
                self.dir = 'LEFT'
            else:
                self.dir = 'UP'


        if action == [1, 0, 0]:
            update()
        elif action == [0, 1, 0]:
            left()
            update()
        elif action == [0, 0, 1]:
            right()
            update()
        self._check_bound(window_size, size)

        if (self.x, self.y) == (food.x, food.y):
            self.contains_food = True
        else:
            self.contains_food = False
            


    def _copy(self):
        a = Body(self.x, self.y)
        a.contains_food = self.contains_food
        return a

