# food class

from block import Block


class Food(Block):
    def __init__(self, x, y):
        super().__init__(x, y, block_type='FOOD')
