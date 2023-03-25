import pygame
import random
from block import Block
from head import Head
from body import Body
from food import Food
from snake import Snake

pygame.init()

window_size = (300, 300)
snake_size  = 50
head_color = (0, 0, 255)
body_color = (0, 255, 0)
food_color = (255, 0, 0)

score = 0

head_position = (window_size[0] // 2, window_size[1] // 2)

head = Head(head_position[0], head_position[1])

display = pygame.display.set_mode(window_size)


snake = [head_position]

_snake = Snake(head)

def new_food(_snake, window_size, snake_size):
    game_space = []
    for x in range(0, window_size[0], snake_size):
        for y in range(0, window_size[1], snake_size):
            game_space.append((x,y))
    free_space = [l for l in game_space if l not in ([(_snake.head.x, _snake.head.y)] + [(k.x, k.y) for k in _snake.body])]
    (food.x,food.y) = random.choice(free_space)
    


food = Food(0, 0)
new_food(_snake, window_size, snake_size)

def check_bound(head, window_size, size):
    if head.x == -size:
        head.x += window_size[0]
    elif head.x == window_size[0]:
        head.x = 0
    elif head.y == -size:
        head.y += window_size[1]
    elif head.y == window_size[1]:
        head.y = 0
    else:
        pass
    print(head.x, head.y)


def game_state(window_size, snake_size, _snake, food):
    state = []
    for x in range(0, window_size[0], snake_size):
        for y in range(0, window_size[1], snake_size):
            if (x,y) == (_snake.head.x, _snake.head.y):
                state.append(0.50)
            elif (x,y) in [(k.x, k.y) for k in _snake.body]:
                state.append(0.25)
            elif (x,y) == (food.x, food.y):
                state.append(0.75)
            else:
                state.append(1.00)
    return state

def main(display, window_size, snake_size, head_color, head_position, food, snake, score, head, _snake):
    running = True
    history = []
    while running:
        state = game_state(window_size, snake_size, _snake, food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return history

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if head.dir == 'UP':
                        action = [1, 0, 0]
                    elif head.dir == 'RIGHT':
                        action = [0, 1, 0]
                    elif head.dir == 'LEFT':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_DOWN:
                    if head.dir == 'DOWN':
                        action = [1, 0, 0]
                    elif head.dir == 'LEFT':
                        action = [0, 1, 0]
                    elif head.dir == 'RIGHT':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_LEFT:
                    if head.dir == 'LEFT':
                        action = [1, 0, 0]
                    elif head.dir == 'UP':
                        action = [0, 1, 0]
                    elif head.dir == 'DOWN':
                        action = [0, 0, 1]
                    else:
                        return history

                if event.key == pygame.K_RIGHT:
                    if head.dir == 'RIGHT':
                        action = [1, 0, 0]
                    elif head.dir == 'DOWN':
                        action = [0, 1, 0]
                    elif head.dir == 'UP':
                        action = [0, 0, 1]
                    else:
                        return history

                history = [(state, action)] + history

                check_bound(head, window_size, snake_size)
                _snake._update(action, food)
                print(_snake.head.contains_food)


                if _snake.head.contains_food:
                    score += 1
                    new_food(_snake, window_size, snake_size)


        empty_space = []
        for row in range(0, window_size[1], snake_size):
            r = []
            for col in range(0, window_size[0], snake_size):
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

game = main(display, window_size, snake_size, head_color, head_position, food, snake, score, head, _snake)
pygame.quit()

print(game)
