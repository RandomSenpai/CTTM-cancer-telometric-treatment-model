import numpy as np
import matplotlib.pyplot as plt

# telomerase-targeting therapy
def drug_dosage(t):
  return 0.6 if t > 50 else 0.0
def growth_rate(L):
  if L <= L_min:
    return 0
  return r0 * (L-L_min) / (L0 - L_min)


time_steps = 200

# initial conditions
N = np.zeros(time_steps)
L = np.zeros(time_steps)

N[0] = 1000 # initial amount of cancer cells at (0,0)
L[0]= 10.0 # telomere length at (0,0)
L0 = L[0] # max telomere length

# parameters
shortening = 0.05 # how much the telomeres shorten per division
repair = 0.04 # how much telemerase is able to repair per division
T = 0.9 # telomerase activity
L_min = 5.0 # senescence threshold
growth_rate = 1.1
r0 = 0.25

# time evolution loop
for t in range(1, time_steps):
  # medicine dosage (obviously will start with nothing)
  D = drug_dosage(t)
  # update telomere length loop
  if L[t-1] > L_min:
    # update telomere length (only if dividing)
    L[t] = L[t-1] - shortening + repair * T * (1-D)
    L[t] = min(L[t], L0) # cap telomere length
    # exponential growth with telomere constraint


# actually plotting results
plt.figure()
plt.plot(N, label= "Cancer Cell Population")
plt.xlabel("Time")
plt.ylabel("Cells")
plt.legend()
plt.show()

plt.figure()
plt.plot(L, label="Average Telomere Length")
plt.axhline(L_min, linestyle='--', label="Senescence Threshold")
plt.legend()
plt.show()

r0 = 0.25 # max intrinsic growth rate
