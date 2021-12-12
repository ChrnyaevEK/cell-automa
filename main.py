import cellpylib as cpl
cellular_automaton = cpl.init_simple2d(10, 10, 0)


# --------------------------------------- OSCILLATORS
# Blinker
cellular_automaton[:, [3], [4]] = 1
cellular_automaton[:, [4], [4]] = 1
cellular_automaton[:, [5], [4]] = 1

# Toad
# cellular_automaton[:, [3], [4, 5, 6]] = 1
# cellular_automaton[:, [4], [3, 4, 5]] = 1

# Beacon
# cellular_automaton[:, [3], [2, 3]] = 1
# cellular_automaton[:, [4], [2, 3]] = 1
# cellular_automaton[:, [5], [4, 5]] = 1
# cellular_automaton[:, [6], [4, 5]] = 1

# --------------------------------------- STILL LIFE
# Block pattern
# cellular_automaton[:, [4, 5], [5, 5]] = 1
# cellular_automaton[:, [4, 5], [4, 4]] = 1

# Bi-block pattern
# cellular_automaton[:, [4, 5], [2, 2]] = 1
# cellular_automaton[:, [4, 5], [3, 3]] = 1
#
# cellular_automaton[:, [4, 5], [5, 5]] = 1
# cellular_automaton[:, [4, 5], [6, 6]] = 1

# Hive pattern
# cellular_automaton[:, [3, 3], [4, 5]] = 1
# cellular_automaton[:, [4, 4], [3, 6]] = 1
# cellular_automaton[:, [5, 5], [4, 5]] = 1

# --------------------------------------- SPACESHIP
# cellular_automaton[:, [4], [5]] = 1
# cellular_automaton[:, [5], [6]] = 1
# cellular_automaton[:, [6], [4, 5, 6]] = 1

# Evolve the cellular automaton for 60 time steps
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=360, neighbourhood='Moore',
                                  apply_rule=cpl.game_of_life_rule, memoize='recursive')

cpl.plot2d_animate(cellular_automaton)
