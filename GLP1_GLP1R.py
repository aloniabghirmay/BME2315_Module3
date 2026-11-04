# ligand_receptor.py

import numpy as np
import matplotlib.pyplot as plt

def Fact(G, S, Kd1, Kd2):
    """Fractional receptor activation by GLP-1 and semaglutide."""
    return (Kd2 * G + Kd1 * S) / (Kd1 * Kd2 + Kd2 * G + Kd1 * S)

Kd1 = 0.17    # Dissociation constant for GLP-1 (nM), how strongly GLP-1 binds to the receptor
Kd2 = 0.38     # Dissociation constant for semaglutide (nM), how strongly semaglutide binds to the receptor

G_fasting = 0.0150    # GLP-1 concentration during fasting (nM), natural GLP-1 concentration when you haven't eaten
G_fed = 0.040        # GLP-1 concentration after eating (nM), natural GLP-1 concentration after eating

S = np.logspace(-2, 4, 500)  # Semaglutide concentration (nM), different semaglutide concentrations we want to test

plt.figure()  # Creates a new figure for the graph

# Plots receptor activation at fasting GLP-1 levels as semaglutide concentration increases
plt.semilogx(S, Fact(G_fasting, S, Kd1, Kd2), lw=2, label="Fasting GLP-1")

# Plots receptor activation at fed GLP-1 levels as semaglutide concentration increases
plt.semilogx(S, Fact(G_fed, S, Kd1, Kd2), lw=2, label="Fed GLP-1")

plt.ylim(0, 1)  # Sets the y-axis from 0 (0% activation) to 1 (100% activation)

plt.xlabel("Semaglutide concentration (nM, log scale)")  # Labels the x-axis with semaglutide concentration
plt.ylabel("Fraction active (Fact)")  # Labels the y-axis with the fraction of activated receptors

plt.title("GLP-1R Activation by Semaglutide")  # Adds a title to the graph

plt.legend()  # Adds a legend to distinguish fasting and fed GLP-1 curves

plt.show()  # Displays the completed graph