from stable_baselines3 import TD3
import numpy as np

# Función para entrenar TD3
def entrenar_td3(env, timesteps):
    model = TD3("MlpPolicy", env, verbose=1, learning_rate=0.001)
    
    # Lista para almacenar las recompensas de cada episodio
    rewards = []
    
    # Entrenar el modelo
    for _ in range(timesteps // 50):  # Cada 50 pasos para simular episodios
        model.learn(total_timesteps=50)
        
        # Evaluar el agente
        episode_reward = 0
        for _ in range(50):
            obs = env.reset()[0]  # Resetear el entorno
            done = False
            while not done:
                action, _ = model.predict(obs)
                obs, reward, done, _, _ = env.step(action)
                episode_reward += reward
        
        rewards.append(episode_reward)
    
    return rewards
