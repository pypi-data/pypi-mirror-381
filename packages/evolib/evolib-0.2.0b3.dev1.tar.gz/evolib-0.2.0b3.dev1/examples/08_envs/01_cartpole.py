import numpy as np
from evolib import Population, Individual, resume_or_create
from evolib.envs.gym_wrapper import GymEnvWrapper

CONFIG_FILE = "./configs/01_cartpole.yaml"
MAX_STEPS = 500

# init environment once (can be reused for all individuals)
cartpole_env = GymEnvWrapper("CartPole-v1", max_steps=MAX_STEPS)


def eval_cartpole_fitness(indiv: Individual) -> None:
    """Assign fitness to an individual by running one CartPole episode."""
    fitness = cartpole_env.evaluate(indiv, module="brain")
    indiv.fitness = -fitness

if __name__ == "__main__":
    pop = resume_or_create(
        CONFIG_FILE,
        fitness_function=eval_cartpole_fitness,
        run_name="08_cartpole",
    )

#    pop.run()  # normal EvoLib evolution

    for gen in range(pop.max_generations):
        pop.run_one_generation()

        # alle 20 Generationen besten Agenten visualisieren
        if gen % 20 == 0:
            best = pop.best()
            #print(best.print_status())
            gif = cartpole_env.visualize(best, gen)
            print(f"Saved: {gif}")
