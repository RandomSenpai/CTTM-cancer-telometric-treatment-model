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
