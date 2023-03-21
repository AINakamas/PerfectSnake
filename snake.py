import pygame
import random

pygame.init()

window_size = (300, 300)
snake_size  = 50
head_color = (0, 0, 255)
body_color = (0, 255, 0)
food_color = (255, 0, 0)
background_color = (125, 125, 123)

score = 0

head_position = (window_size[0] // 2, window_size[1] // 2)

display = pygame.display.set_mode(window_size)


snake = [head_position]

def new_food(snake, window_size, snake_size):
    game_space = []
    for x in range(0, window_size[0], snake_size):
        for y in range(0, window_size[1], snake_size):
            game_space.append((x,y))
    free_space = [x for x in game_space if x not in snake]
    if free_space == []:
        return False
    return random.choice(free_space)

food_position = new_food(snake, window_size, snake_size)

def check_bound(head_position, window_size, size):
    if head_position[0] == -size:
        return (window_size[0] - size, head_position[1])
    elif head_position[0] == window_size[0]:
        return (0, head_position[1])
    elif head_position[1] == -size:
        return (head_position[0], window_size[1] - size)
    elif head_position[1] == window_size[1]:
        return (head_position[0], 0)
    else:
        return head_position

def update_snake(new_head, old_snake):
    return [new_head] + old_snake[:-1]

def game_state(window_size, snake_size, snake, food_position):
    state = []
    for x in range(0, window_size[0], snake_size):
        for y in range(0, window_size[1], snake_size):
            if (x,y) == snake[0]:
                state.append(0.50)
            elif (x,y) in snake[1:]:
                state.append(0.25)
            elif (x,y) == food_position:
                state.append(0.75)
            else:
                state.append(1.00)
    return state

def main(display, window_size, snake_size, head_color, background_color, head_position, food_position, snake, score):
    running = True
    history = []
    while running:
        state = game_state(window_size, snake_size, snake, food_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    new_head = (snake[0][0], snake[0][1] - snake_size)
                    action = [1, 0, 0, 0]

                if event.key == pygame.K_DOWN:
                    new_head = (snake[0][0], snake[0][1] + snake_size)
                    action = [0, 1, 0, 0]

                if event.key == pygame.K_LEFT:
                    new_head = (snake[0][0] - snake_size, snake[0][1])
                    action = [0, 0, 1, 0]

                if event.key == pygame.K_RIGHT:
                    new_head = (snake[0][0] + snake_size, snake[0][1])
                    action = [0, 0, 0, 1]

                history = [(state, action)] + history
                
                new_head = check_bound(new_head, window_size, snake_size)
                snake = update_snake(new_head, snake)

        if snake[0] in snake[2:]:
            running = False

        if snake[0] == food_position:
            score += 1
            print("Score: ", score)
            snake = [snake[0], food_position] + snake[1:]
            food_position = new_food(snake, window_size, snake_size)
            if not food_position:
                print("You win!!!!")
                break 


        display.fill(background_color)

        for x in snake[1:]:
            pygame.draw.rect(display, body_color, (x[0], x[1], snake_size - 2, snake_size - 2))

        pygame.draw.rect(display, head_color, (snake[0][0], snake[0][1], snake_size - 2, snake_size - 2))
        
        pygame.draw.rect(display, food_color, (food_position[0], food_position[1], snake_size - 2, snake_size - 2))

        pygame.display.flip()
    
    return history






print("Score: ", score)

game = main(display, window_size, snake_size, head_color, background_color, head_position, food_position, snake, score)
pygame.quit()

print(game)
