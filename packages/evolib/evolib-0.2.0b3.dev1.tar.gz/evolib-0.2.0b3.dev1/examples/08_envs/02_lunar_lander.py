import numpy as np
from evolib import Population, Individual, resume_or_create
from evolib.envs.gym_wrapper import GymEnvWrapper

CONFIG_FILE = "./configs/02_lunarlander.yaml"
MAX_STEPS = 500

# init environment once (can be reused for all individuals)
lunar_env = GymEnvWrapper("LunarLander-v3", max_steps=MAX_STEPS)


def eval_lunar_fitness(indiv: Individual) -> None:
    """Assign fitness to an individual by running one LunarLander episode."""
    fitness = lunar_env.evaluate(indiv, module="brain")
    indiv.fitness = -fitness

if __name__ == "__main__":
    pop = resume_or_create(
        CONFIG_FILE,
        fitness_function=eval_lunar_fitness,
        run_name="02_lunarlander",
    )

    for gen in range(pop.max_generations):
        pop.run_one_generation()

        # alle 20 Generationen besten Agenten visualisieren
        if gen % 10 == 0:
            best = pop.best()
            #print(best.print_status())
            gif = lunar_env.visualize(best, gen)
            print(f"Saved: {gif}")
