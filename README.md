# Evaluación de Desempeño del Robot Fetch-Reach

Este proyecto de aprendizaje por refuerzo compara algoritmos en un entorno de manipulación robótica. Utilizando Gymnasium-Robotics y el motor de física MuJoCo, evaluamos el rendimiento de diferentes algoritmos de RL en el entorno **FetchReach-v3**.

## Integrantes
- Martin Isla P.
- Javier Leiva U.
- Martina Lara
- Macarena Madrid B.

## Descripción del Proyecto y Motivación

En este proyecto, nos centramos en el entorno FetchReach-v3, donde el **robot Fetch 7-DoF** debe mover su efector final hasta una posición objetivo dentro de su espacio de trabajo. La motivación principal es analizar cómo diferentes métodos de actualización de valores afectan el rendimiento y estabilidad de un agente en esta tarea de manipulación robótica.

### Entorno: FetchReach-v3

El entorno de FetchReach incluye un manipulador móvil de 7 grados de libertad (7-DoF) con una pinza de dos dedos, capaz de moverse en coordenadas cartesianas. La tarea consiste en mover el efector final a una posición aleatoria en el espacio de trabajo.

Más detalles en la [documentación de Gymnasium-Robotics](https://robotics.farama.org/index.html).

### Algoritmos Utilizados

Implementamos y comparamos los siguientes algoritmos de aprendizaje por refuerzo:

- **PPO** (Proximal Policy Optimization): Un método de optimización de políticas desarrollado por Schulman et al., 2017. [Paper](https://arxiv.org/abs/1707.06347)
- **TD3** (Twin Delayed Deep Deterministic Policy Gradient): Una mejora sobre DDPG que incluye una política de retraso doble. Fujimoto et al., 2018. [Paper](https://arxiv.org/abs/1802.09477)

Ambos algoritmos se evaluarán con recompensas **sparse** y **dense** para ver cómo afectan el aprendizaje y la estabilidad del agente.

## Requisitos

Para ejecutar el proyecto, asegúrate de tener:

- **Python** (versión recomendada: 3.8 o superior)
- **Gymnasium** (versión 1.0.0)
- **Gymnasium-Robotics** (versión 1.3.1)
- **Stable-baselines3** (versión 2.4.0a11)
- **MuJoCo** (versión 3.1.6)

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/usuario/rl-proyecto.git
   cd rl-proyecto

2. Instala las dependencias:

   ```bash
   pip install gymnasium==1.0.0
   pip install gymnasium-robotics==1.3.1
   pip install stable-baselines3==2.4.0a11
   pip install mujoco==3.1.6

3. Asegúrate de tener MuJoCo y Gymnasium-Robotics configurados correctamente en tu entorno.

## Ejecución

Para entrenar el agente en FetchReach-v3, puedes ejecutar:

```bash
python main.py --env FetchReach-v3 --algo PPO --reward sparse
```

Modifica los parámetros `--algo` y `--reward` para cambiar el algoritmo o el tipo de recompensa.


## Resultados y análisis
El objetivo final es comparar el desempeño entre PPO y TD3 en cuanto a:

- Rendimiento: tasa de éxito al alcanzar la posición objetivo
- Estabilidad: variación en los valores de recompensa a lo largo del tiempo

## Créditos
Este proyecto fue desarrollado como parte del curso de Aprendizaje por Refuerzo en colaboración con los integrantes mencionados arriba.



