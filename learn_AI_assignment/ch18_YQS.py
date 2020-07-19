## This is course material for Introduction to Modern Artificial Intelligence
## Class 18 Example code: breakout.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# # Please make sure to install openAI gym module and atari module
# https://github.com/openai/gym

import gym
import numpy as np
import cv2
import random
import os
import keras
from keras import backend as K
from collections import deque
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import tensorflow as tf


def huber_loss(a, b, in_keras=True):
    error = a - b
    quadratic_term = error * error / 2
    linear_term = abs(error) - 1 / 2
    use_linear_term = (abs(error) > 1.0)
    if in_keras:
        # Keras won't let us multiply floats by booleans, so we explicitly cast the booleans to floats
        use_linear_term = K.cast(use_linear_term, 'float32')
    return use_linear_term * linear_term + (1 - use_linear_term) * quadratic_term


class DQNAgent:
    def __init__(self, state_size, action_size, fully_connected_size=24, height=210, width=160):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=1000000)
        self.gamma = 0.99  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.99999
        self.learning_rate = 0.00025
        self.fully_connected_size = fully_connected_size
        self.model = self._build_model()
        self.height = height
        self.width = width

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        initializer = keras.initializers.VarianceScaling(scale=2)
        model = Sequential()
        model.add(Dense(self.fully_connected_size, input_dim=self.state_size, activation='relu',
                        kernel_initializer=initializer))
        model.add(Dense(self.fully_connected_size, activation='relu', kernel_initializer=initializer))
        model.add(Dense(self.action_size, activation='linear'))
        optimizer = keras.optimizers.RMSprop(self.learning_rate, rho=0.95, epsilon=0.01)
        model.compile(loss=huber_loss,
                      optimizer=optimizer)
        return model

    def remember(self, state, action, reward, next_state, dead):
        self.memory.append((state, action, reward, next_state, dead))

    def act(self, state):
        # For breakout the act range is {1, 2, 3}需要时不时的出现一个随机扰动，以防训练的结果跑偏
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, dead in minibatch:
            target = reward
            if not dead:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)

    def compute_state(self, observe, next_observe):
        # First update the state of the paddle. Color pattern is [200 72 72]
        global height, width

        if not 'paddle_states' in globals():
            global paddle_states, ball_states
            # paddle左右两端的坐标，ball的（x, y)坐标，所以一幅图像有4维数据，每四张为一组，就是16维的数据，其中paddle和ball各占8维
            paddle_states = deque([0] * (self.state_size // 2), maxlen=self.state_size // 2)
            ball_states = deque([0] * (self.state_size // 2), maxlen=self.state_size // 2)

        paddle = [None, None]
        for w in range(8, width - 8):
            # 已经知道了paddle就在height-20的高度位置，通过颜色来寻找paddle的具体位置
            if (next_observe[height - 20, w] == [200, 72, 72]).all():
                # We are on a paddle
                if paddle[0] is None:
                    # 把第一次出现的w放在paddle[0],表示最左边的坐标，把以后出现的w都不断更新的paddle[1],最后一个w就是最右边的坐标
                    paddle[0] = w
                else:
                    paddle[1] = w
        paddle_states.append(paddle[0]);
        paddle_states.append(paddle[1])
        # Second update the state of the ball.
        ball = []
        for h in range(20, height - 21):
            for w in range(8, width - 8):
                # 下一帧图像如果和上一帧图像有区别那么就把变化的位置存下来
                if (next_observe[h, w] != observe[h, w]).all() and (observe[h, w] == [0, 0, 0]).all():
                    ball.append([h, w])

        if ball:
            # 取平均求得球的中心位置坐标
            ball = np.average(ball, axis=0)
        else:
            ball = [0, 0]

        ball_states.append(ball[0]);
        ball_states.append(ball[1])

        state_list = list(paddle_states)
        state_list.extend(list(ball_states))
        state = np.array(state_list)
        state = state.astype('float32')
        state = np.reshape(state, (1, self.state_size))
        return state


if __name__ == "__main__":

    GAME_TITLE = 'BreakoutDeterministic-v4'
    EPISODES = 1000000

    CONTROL_RL = 0
    CONTROL_MANUAL = 1
    CONTROL_RANDOM = 2

    control = CONTROL_RL  # This controls how to play the game
    load_dqn_model = False  # Whether to load a model
    save_dqn_model = True  # Whether to save a model
    display_game = False  # Whether to display the game graphics, only effective for RL learning
    batch_size = 32
    fully_connected_size = 256
    Q_look_ahead = 4  # How many frames used for calculating the Q function

    # Deterministic-v4 version use 4 actions
    env = gym.make(GAME_TITLE)

    # Each frame contains 4 states: paddle left end, paddle right end, ball x, ball y
    observe = env.reset()
    height, width, channel = observe.shape
    state_size = 4 * Q_look_ahead
    action_size = 4  # Action 2: Move left. Action 3: Move right
    agent = DQNAgent(state_size, action_size, fully_connected_size, height, width)
    path = os.path.dirname(os.path.abspath(__file__))
    model_file_name = path + '/breakout-dqn-' + str(fully_connected_size) + '.h5'
    if load_dqn_model:
        print('Loading a pre-trained model ...')
        agent.load(model_file_name)
    for e in range(EPISODES):
        # Initialize a new set of game
        observe = env.reset()
        next_observe, reward, done, next_info = env.step(1)
        state = agent.compute_state(observe, next_observe)
        score = 0;
        replay_freq = 0
        while not done:
            if display_game or control != CONTROL_RL:
                # The user can choose to not display the game
                img = cv2.cvtColor(next_observe, cv2.COLOR_RGB2BGR)
                cv2.imshow("Breakout", img)

                if control == CONTROL_RL:
                    key = cv2.waitKey(1)
                else:
                    key = cv2.waitKey(100)
                if key == ord('q'):
                    quit()

            if control == CONTROL_MANUAL:
                # Controlling breakout only takes action 1, 2, 3
                action = 1
                if key > 0:
                    key = chr(key & 255)
                    if key == 'j' or key == 'J':
                        action = 3
                    elif key == 'l' or key == 'L':
                        action = 2
            elif control == CONTROL_RANDOM:
                action = env.action_space.sample()
            else:
                action = agent.act(state)

            observe = next_observe;
            info = next_info
            next_observe, reward, done, next_info = env.step(action)
            if done or (next_info['ale.lives'] != info['ale.lives']):
                # Redefine death equal either done or losing a life
                dead = True
            else:
                dead = False

            reward = reward if not dead else -1
            if reward == 1:
                # add positive reward to score
                score += 1
            # 用视觉的方法获得下一步的state
            next_state = agent.compute_state(observe, next_observe)
            agent.remember(state, action, reward, next_state, dead)
            state = next_state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, score, agent.epsilon))
                break

            replay_freq += 1
            # 每隔4帧训练一次
            if replay_freq == 4 and len(agent.memory) > batch_size:
                replay_freq = 0
                agent.replay(batch_size)

            if e % 10 == 0 and save_dqn_model:
                agent.save(model_file_name)
