# snake class

from body import Body

class Snake():
    def __init__(self, head):
        self.head = head
        self.body = [Body(head.x, head.y + 50)]


    def _update(self, action, food, window_size, size):
        if self.body[-1].contains_food:
            self.body.append(Body(self.body[-1].x, self.body[-1].y))
            self.body[-2].contains_food = False
        a = self.head._copy()
        self.head._update(action, food, window_size, size)
        for i in range(len(self.body)):
            b = self.body[i]._copy()
            self.body[i]._update(a)
            a = b._copy()


    def _tail_collision(self):
        return (self.head.x, self.head.y) in [(k.x, k.y) for k in self.body]


    def _draw(self, display):
        self.head._draw(display)
        l = len(self.body)
        for i in range(l):
            self.body[i]._draw(display, 20 - i*(15 / l))
