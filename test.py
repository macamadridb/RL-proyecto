import gymnasium as gym

# Crear el entorno FetchReach-v3
env = gym.make("FetchReach-v2", render_mode="human")
# Reiniciar el entorno con una semilla fija
observation, info = env.reset(seed=42)

# Ejecutar 1000 pasos en el entorno
for _ in range(1000):
   action = env.action_space.sample()  # User-defined policy function
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()