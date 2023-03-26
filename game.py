import pygame
import random
from block import Block
from head import Head
from body import Body
from food import Food
from snake import Snake



WINDOW_SIZE      = (300, 300)
SIZE             = 50

class Game():
    def __init__(self):
        self.score       = 0
        self.window_size = WINDOW_SIZE
        self.size        = SIZE
        self.display     = pygame.display.set_mode(WINDOW_SIZE)
        self.snake       = Snake(Head(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

score = 0

display = pygame.display.set_mode(WINDOW_SIZE)

_snake = Snake(Head(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

def new_food(_snake, WINDOW_SIZE, SIZE):
    game_space = []
    for x in range(0, WINDOW_SIZE[0], SIZE):
        for y in range(0, WINDOW_SIZE[1], SIZE):
            game_space.append((x,y))
    free_space = [l for l in game_space if l not in ([(_snake.head.x, _snake.head.y)] + [(k.x, k.y) for k in _snake.body])]
    (food.x,food.y) = random.choice(free_space)
    


food = Food(0, 0)
new_food(_snake, WINDOW_SIZE, SIZE)

def game_state(WINDOW_SIZE, SIZE, _snake, food):
    state = []
    for x in range(0, WINDOW_SIZE[0], SIZE):
        for y in range(0, WINDOW_SIZE[1], SIZE):
            if (x,y) == (_snake.head.x, _snake.head.y):
                state.append(0.50)
            elif (x,y) in [(k.x, k.y) for k in _snake.body]:
                state.append(0.25)
            elif (x,y) == (food.x, food.y):
                state.append(0.75)
            else:
                state.append(1.00)
    return state

def main(display, WINDOW_SIZE, SIZE, food, score, _snake):
    running = True
    history = []
    while running:
        state = game_state(WINDOW_SIZE, SIZE, _snake, food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return history

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if _snake.head.dir == 'UP':
                        action = [1, 0, 0]
                    elif _snake.head.dir == 'RIGHT':
                        action = [0, 1, 0]
                    elif _snake.head.dir == 'LEFT':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_DOWN:
                    if _snake.head.dir == 'DOWN':
                        action = [1, 0, 0]
                    elif _snake.head.dir == 'LEFT':
                        action = [0, 1, 0]
                    elif _snake.head.dir == 'RIGHT':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_LEFT:
                    if _snake.head.dir == 'LEFT':
                        action = [1, 0, 0]
                    elif _snake.head.dir == 'UP':
                        action = [0, 1, 0]
                    elif _snake.head.dir == 'DOWN':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_RIGHT:
                    if _snake.head.dir == 'RIGHT':
                        action = [1, 0, 0]
                    elif _snake.head.dir == 'DOWN':
                        action = [0, 1, 0]
                    elif _snake.head.dir == 'UP':
                        action = [0, 0, 1]
                    else:
                        return history

                history = [(state, action)] + history
                _snake._update(action, food, WINDOW_SIZE, SIZE)
                
                if _snake._tail_collision():
                    return history

                if _snake.head.contains_food:
                    score += 1
                    print("Score: ", score)
                    new_food(_snake, WINDOW_SIZE, SIZE)


        empty_space = []
        for row in range(0, WINDOW_SIZE[1], SIZE):
            r = []
            for col in range(0, WINDOW_SIZE[0], SIZE):
                r.append(Block(row, col))
            empty_space.append(r)

        for row in empty_space:
            for block in row:
                block._draw(display)


        _snake._draw(display)

        food._draw(display)

        pygame.display.flip()

    return history






print("Score: ", score)

game = main(display, WINDOW_SIZE, SIZE, food, score, _snake)
pygame.quit()

print(game)
