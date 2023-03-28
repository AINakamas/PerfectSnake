# block that represents empty space

from pygame.draw import rect


BACKGROUND_COLOR = (125, 125, 123)
HEAD_COLOR       = (0, 0, 255)
BODY_COLOR       = (0, 255, 0)
FOOD_COLOR       = (255, 0, 0)
EMPTY_REP        = [1.0, 0, 0, 0]
HEAD_REP         = [0, 1.0, 0, 0]
BODY_REP         = [0, 0, 1.0, 0]
FOOD_REP         = [0, 0, 0, 1.0]




class Block:
    def __init__(self, x, y, size= 50, block_type='EMPTY'):
        self.x     = x
        self.y     = y
        self.size  = size 

        def rep_col(block_type):
            if block_type == 'EMPTY':
                return EMPTY_REP, BACKGROUND_COLOR 
            elif block_type == 'HEAD':
                return HEAD_REP, HEAD_COLOR 
            elif block_type == 'BODY':
                return BODY_REP, BODY_COLOR 
            else:
                return FOOD_REP, FOOD_COLOR 

        self.rep, self.color = rep_col(block_type)

    def _draw(self, display):
        if self.color == BACKGROUND_COLOR or self.color == FOOD_COLOR:
            rect(display, self.color, (self.x, self.y, self.size, self.size))
        else:
            rect(display, self.color, (self.x+1, self.y+1, self.size-2, self.size-2))
        
