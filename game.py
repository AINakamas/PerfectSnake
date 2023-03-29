import gym
import pygame
import random
from block import Block
from head import Head
from body import Body
from food import Food
from snake import Snake
import gym
from gym import envs
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

WINDOW_SIZE      = (200, 200)
SIZE             = 50

class Game():
    def __init__(self):
        self.score       = 0
        self.window_size = WINDOW_SIZE
        self.size        = SIZE
        self.display     = pygame.display.set_mode(WINDOW_SIZE)
        self.snake       = Snake(Head(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        self.food        = Food(0, 0) 
        self.win_flag    = False
        self.AiTraining  = True
        self.history     = []


    def _model(states,actions):
        model= Sequential()
        model.add(Flatten(input_shape=(1,states)))
        model.add(Dense(24,activation="relu"))
        model.add(Dense(actions,activation="linear"))
        return model

    def _build_agent(model, actions):
        policy= BoltzmannQPolicy()
        memory= SequentialMemory(limit=50000, window_length=1)
        dqn= DQNAgent(model,mempry=memory, policy=policy,nb_actions=actions,nb_steps_warmup=10,target_model_update=1e-2)
        return dqn

    def _new_food(self):
        game_space = []
        for x in range(0, self.window_size[0], self.size):
            for y in range(0, self.window_size[1], self.size):
                game_space.append((x,y))
        free_space = [l for l in game_space if l not in ([(self.snake.head.x, self.snake.head.y)] + [(k.x, k.y) for k in self.snake.body])]
        if free_space:
            (self.food.x, self.food.y) = random.choice(free_space)
        else:
            self.win_flag = True

    def _game_state(self):
        state = []
        for x in range(0, self.window_size[0], self.size):
            col = []
            for y in range(0, self.window_size[1], self.size):
                if (x,y) == (self.snake.head.x, self.snake.head.y):
                    col.append(self.snake.head.rep)
                elif (x,y) in [(k.x, k.y) for k in self.snake.body]:
                    col.append(self.snake.body[0].rep)
                elif (x,y) == (self.food.x, self.food.y):
                    col.append(self.food.rep)
                else:
                    col.append(Block(0,0).rep)
            state.append(col)
        return state

    def main(self):
        running = True
        #env= gym.make()
        print("Score: ", self.score)
        if(self.AiTraining == False):
         while running:
            state = self._game_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                if self.win_flag:
                    print("YOU WIN!!!!!!!!")
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        if self.snake.head.dir == 'UP':
                            action = [1, 0, 0]
                        elif self.snake.head.dir == 'RIGHT':
                            action = [0, 1, 0]
                        elif self.snake.head.dir == 'LEFT':
                            action = [0, 0, 1]
                        else:
                            running = False

                    if event.key == pygame.K_DOWN:
                        if self.snake.head.dir == 'DOWN':
                            action = [1, 0, 0]
                        elif self.snake.head.dir == 'LEFT':
                            action = [0, 1, 0]
                        elif self.snake.head.dir == 'RIGHT':
                            action = [0, 0, 1]
                        else:
                            running = False

                    if event.key == pygame.K_LEFT:
                        if self.snake.head.dir == 'LEFT':
                            action = [1, 0, 0]
                        elif self.snake.head.dir == 'UP':
                            action = [0, 1, 0]
                        elif self.snake.head.dir == 'DOWN':
                            action = [0, 0, 1]
                        else:
                            running = False

                    if event.key == pygame.K_RIGHT:
                        if self.snake.head.dir == 'RIGHT':
                            action = [1, 0, 0]
                        elif self.snake.head.dir == 'DOWN':
                            action = [0, 1, 0]
                        elif self.snake.head.dir == 'UP':
                            action = [0, 0, 1]
                        else:
                            running = False

                    self.history.append((state, action))
                    self.snake._update(action, self.food, self.window_size, self.size)
                    
                    if self.snake._tail_collision():
                        running = False

                    if self.snake.head.contains_food:
                        self.score += 1
                        print("Score: ", self.score)
                        self._new_food()
                    
            empty_space = []
            for row in range(0, WINDOW_SIZE[1], SIZE):
                r = []
                for col in range(0, WINDOW_SIZE[0], SIZE):
                    r.append(Block(col, row))
                empty_space.append(r)

            for row in empty_space:
                for block in row:
                    block._draw(self.display)


            self.snake._draw(self.display)

            self.food._draw(self.display)

            pygame.display.flip()
        else:
            env=gym.make('SpaceInvaders-v0')
            height, width, channels= env.observation_space.shape
            actions= env.action_space.shape
            actions= [[1,0,0],[0,1,0],[0,0,1]]
            states=  [[1.0, 0, 0, 0],[0, 1.0, 0, 0],[0, 0, 1.0, 0],[0, 0, 0, 1.0]]
            episodes= 10
            for episode in episodes:
                state= env.reset()
                done= False
                score=0
                while not done:
                    env.render()
                    action= random.choice([0,1,2,3,4,5])
                    n_state,reward,done,info= env.step(action)
                    score+=reward
                print('Episode{} Score{}'.format(episode,score))
            env.close()
            model= self._model(len(states), len(actions))
            dqn= self._build_agent(model,len(actions))
            dqn.compile(Adam(lr=1e-3),metrics=['mae'])
            dqn.fit()




game = Game()
game.main()
