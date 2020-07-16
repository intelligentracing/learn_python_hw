## This is course material for Introduction to Modern Artificial Intelligence
## Class 17 Example code: cartpole_dqn.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to install openAI gym module
# https://github.com/openai/gym
import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

EPISODES = 1000


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):#贪心算法，为了权衡state下一步的action是随机选择还是从已经有Q值的action中选取
        #选取原则是如果随机值小于设置的贪心值，说明算法认为随机选取action会带来更大的收益
        #epsilon会随着神经网络不断训练更新reward值自身不断减小，慢慢的就会从随机选取action变为
        #根据action所对应的reward值来选取该步，相当于更新了Q地图中的reward值
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        # 拿到当前state经过predict后可行的action的Q值
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action Q大的那个action

    def replay(self, batch_size):
        #minibatch 每次就32个训练数据
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                #如果没有gameover就对next_state进行Q值的更新，更新其中第[0]个action的Q值，该公式依据bellman Equation
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            #预测出来的也是下一步action的reward，因为有两个action所以有target_f有两个值
            target_f = self.model.predict(state)
            #target是state的准确Q值，将其赋值给predict(state)中的Q值
            target_f[0][action] = target
            #然后就有了测试数据state 和其类别target_f,可以进行模型训练，优化模型，使其predict变得越来越准确
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:#更新贪婪度
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    # 查看这个环境中observation的特征有多少个，返回int
    state_size = env.observation_space.shape[0]
    # 查看这个环境中可用的action有多少个，返回int
    action_size = env.action_space.n
    # 小车两个state，环境两个state
    agent = DQNAgent(state_size, action_size)
    # agent.load("./save/cartpole-dqn.h5")
    done = False
    # 每32次记录的步骤更新DQN网络
    batch_size = 32

    for e in range(EPISODES):
        # 用于一个世代（done）后环境的重启，获取回合的第一个state
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        for time in range(500):
            # env.render()
            # agent.act根据state获得可以走的下一步有哪些
            action = agent.act(state)
            # 获取下一步的环境、得分、检测是否完成。
            next_state, reward, done, _ = env.step(action)
            # 用于每一步后刷新环境状态
            env.render()
            #如果state做出的action导致game over了，reward就-10，然后把这个state 的这个action的这个reward记录到agent里
            reward = reward if not done else -10
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
            #每达到32次的数据记录就进行一次模型的训练，以更新参数
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
        # if e % 10 == 0:
        #     agent.save("./save/cartpole-dqn.h5")