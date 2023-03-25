# snake class

from body import Body

class Snake():
    def __init__(self, head):
        self.head = head
        self.body = []


    def _update(self, action, food):
        if len(self.body) == 0:
            if self.head.contains_food:
                self.body.append(Body(self.head.x, self.head.y))
            else:
                self.head._update(action, food)
        elif len(self.body) == 1:
            a = self.head._copy
            self.head._update(action, food)
            a.contains_food




    def _tail_collision(self):
        return (self.head.x, self.head.y) in [(k.x, k.y) for k in self.body]


    def _draw(self, display):
        self.head._draw(display)
        for body_part in self.body:
            body_part._draw(display)
