import gymnasium as gym
env = gym.make("FrozenLake-v1",render_mode = "human")

observation, info = env.reset(seed=42)
for _ in range(10):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

# env.close()

