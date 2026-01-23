import numpy as np
import matplotlib.pyplot as plt

time_steps = 200

# initial conditions
N = np.zeros(time_steps)
L = np.zeros(time_steps)

N[0] = 1000 # initial amount of cancer cells at (0,0)
L[0]= 10.0 # telomere length at (0,0)

# parameters
shortening = 0.05 # how much the telomeres shorten per division
repair = 0.04 # how much telemerase is able to repair per division
T = 0.9 # telomerase activity
L_min = 5.0 # senescence threshold
growth_rate = 1.1

# time evolution loop
for t in range(1, time_steps):
  # medicine dosage (obviously will start with nothing)
  M = 0.0
  # update telomere length loop
  L[t] = L[t-1] - shortening + repair * T * (1-D)
  # growth rules
  if L[t] > L_min:
    N[t] = N[t-1] * growth_rate
  else:
    N[t] = N[t-1] * 0.9 # natural decline due to senescence

# actually plotting results
plt.figure()
plt.plot(N, label= "Cancer Cell Population")
plt.xlabel("Time")
plt.ylabel("Cells")
plt.legend()
plt.show()

plt.figure()
plt.plot(L, label="Average Telomere Length")
plt.axhline(L_min, linestyle
