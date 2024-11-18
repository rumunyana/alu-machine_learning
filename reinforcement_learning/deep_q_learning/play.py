import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import GreedyQPolicy
from rl.memory import SequentialMemory
from rl.core import Processor
from gym.wrappers import AtariPreprocessing, FrameStack

class AtariProcessor(Processor):
    """ Processor for Atari 2600 preprocessing for playing """
    def process_observation(self, observation):
        return np.array(observation).astype('float32') / 255.

    def process_reward(self, reward):
        return np.clip(reward, -1., 1.)

def build_model(nb_actions):
    """ CNN model architecture for playing """
    model = Sequential([
        Conv2D(32, (8, 8), strides=4, activation='relu', input_shape=(84, 84, 4)),
        Conv2D(64, (4, 4), strides=2, activation='relu'),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(nb_actions, activation='linear')
    ])
    return model

def play():
    env = gym.make('Breakout-v0')
    env = AtariPreprocessing(env, frame_skip=4, grayscale_obs=True, scale_obs=True)
    env = FrameStack(env, 4)

    nb_actions = env.action_space.n
    model = build_model(nb_actions)  # Ensure this matches the training script

    memory = SequentialMemory(limit=50000, window_length=4)
    policy = GreedyQPolicy()
    processor = AtariProcessor()

    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
                   policy=policy, processor=processor)
    dqn.compile(Adam(lr=0.00025), metrics=['mae'])

    dqn.load_weights('policy.h5')
    dqn.test(env, nb_episodes=10, visualize=True)

if __name__ == '__main__':
    play()
