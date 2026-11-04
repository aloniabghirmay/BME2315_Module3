
import numpy as np
import matplotlib.pyplot as plt

# Fractional receptor activation by GLP1 and semaglutide
def Fact(GLP1, semaglutide, Kd_GLP1, Kd_sema):
    return (GLP1/Kd_GLP1 + semaglutide/Kd_sema) / (1 + GLP1/Kd_GLP1 + semaglutide/Kd_sema)

# Dissociation constants [nM]
Kd_GLP1 = 0.17
Kd_sema = 0.38

# GLP1 concentrations [nM]
GLP1_fasting = 0.015
GLP1_fed = 0.040

# Semaglutide concentration range [nM]
semaglutide = np.logspace(-3, 2, 500)

# Calculate receptor activation for fasting and fed conditions
Fact_fasting = Fact(GLP1_fasting, semaglutide, Kd_GLP1, Kd_sema)
Fact_fed = Fact(GLP1_fed, semaglutide, Kd_GLP1, Kd_sema)

# Calculate baseline activation without semaglutide
baseline_fasting = Fact(GLP1_fasting, 0, Kd_GLP1, Kd_sema)
baseline_fed = Fact(GLP1_fed, 0, Kd_GLP1, Kd_sema)

# Plot concentration-response curves
plt.figure()

plt.semilogx(semaglutide, Fact_fasting, lw=2, label="Fasting GLP1 (0.015 nM)")
plt.semilogx(semaglutide, Fact_fed, lw=2, label="Fed GLP1 (0.040 nM)")

plt.ylim(0, 1)
plt.xlabel("Semaglutide concentration (nM, log scale)")
plt.ylabel("Fraction active (Fact)")
plt.title("GLP1R Activation by GLP1 and Semaglutide")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("GLP1_GLP1R_plot.png", dpi=300)
plt.show()

# Print baseline receptor activation
print("Fasting baseline response:", round(baseline_fasting * 100, 2), "%")
print("Fed baseline response:", round(baseline_fed * 100, 2), "%")
