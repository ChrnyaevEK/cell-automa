import numpy as np
import matplotlib.pyplot as plt

rule = 60  # Number between 0 and 255
size = 100  # Number of cells
steps = 100  # Number of generations


def do_step(x, rb):
    """Calculate a step of an cellular automaton."""
    # The columns contain the L, C, R values of all cells.
    y = np.vstack((np.roll(x, 1), x, np.roll(x, -1))).astype(np.int8)
    # We get the LCR pattern numbers between 0 and 7.
    z = np.sum(y * np.array([[4], [2], [1]]), axis=0).astype(np.int8)
    # We get the patterns given by the rule.
    return rb[7 - z]


def initialize(r, sz, st):
    """Create an elementary cellular automaton"""
    # Compute the binary representation of the rule
    rule_bin = np.array([int(b) for b in np.binary_repr(r, 8)], dtype=np.int8)
    # Prepare matrix
    x = np.zeros((st, sz), dtype=np.int8)
    # Random initial state (1st row)
    x[0, :] = np.random.rand(sz) < .5
    # Simulate by applying step function
    for i in range(st - 1):
        x[i + 1, :] = do_step(x[i, :], rule_bin)
    return x


if __name__ == '__main__':
    axes = plt.gca()
    axes.imshow(initialize(rule, size, steps), interpolation='none', cmap=plt.cm.binary)
    axes.set_axis_off()
    axes.set_title(f"Rule: {rule}")

    plt.show()
