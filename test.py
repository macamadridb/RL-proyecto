import gymnasium as gym
import argparse
import matplotlib.pyplot as plt
from stable_baselines3 import PPO, TD3
from algoritmo_ppo import entrenar_ppo
from algoritmo_td3 import entrenar_td3

# Función para graficar los resultados de rendimiento
def plot_rewards(rewards_ppo, rewards_td3):
    plt.plot(rewards_ppo, label='PPO')
    plt.plot(rewards_td3, label='TD3')
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.title('Comparación de Algoritmos')
    plt.legend()
    plt.show()

# Función principal que ejecuta el entrenamiento y análisis
def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Entrenamiento de modelos RL en FetchReach-v3")
    parser.add_argument('--env', type=str, default='FetchReach-v3', help='Nombre del entorno de Gym')
    parser.add_argument('--algo', type=str, choices=['PPO', 'TD3'], default='PPO', help='Algoritmo de RL a utilizar')
    parser.add_argument('--reward', type=str, choices=['sparse', 'dense'], default='dense', help='Tipo de recompensa')
    parser.add_argument('--timesteps', type=int, default=1000, help='Número total de pasos de entrenamiento')
    args = parser.parse_args()

    # Crear el entorno
    env = gym.make(args.env, render_mode="human")
    env.reward_type = args.reward

    # Imprimir información sobre el entorno
    print("Observation space:", env.observation_space)
    print("Action space:", env.action_space)
    print("Reward type:", env.reward_type)

    # Inicializar listas para almacenar resultados
    rewards_ppo = []
    rewards_td3 = []

    # Entrenar según el algoritmo seleccionado
    if args.algo == 'PPO':
        print("Entrenando PPO...")
        rewards_ppo = entrenar_ppo(env, args.timesteps)
    elif args.algo == 'TD3':
        print("Entrenando TD3...")
        rewards_td3 = entrenar_td3(env, args.timesteps)

    # Graficar los resultados
    plot_rewards(rewards_ppo, rewards_td3)

    # Cerrar el entorno
    env.close()

# Ejecutar el script
if __name__ == "__main__":
    main()
