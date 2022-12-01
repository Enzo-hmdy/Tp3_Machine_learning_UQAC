from matplotlib import pyplot as plt
import pandas as pd
import numpy as np



nb_sample = [130,262,833, ]
score = [0.97,0.992,0.9953]
model = [1,2,3]

# plot score vs nb_sample
plt.plot(nb_sample, score, '-')
plt.axis([0, 1000, 0.9, 1])
plt.xlabel('nb_sample')
plt.ylabel('score')
plt.show()


# plot nbsample and score vs model with 2 différent scale on y axis 00-1000 for nbsample and 0-1 for score
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('model')
ax1.set_ylabel('nb_sample', color=color)
ax1.plot(model, nb_sample, color=color)

ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('score', color=color)  # we already handled the x-label with ax1
ax2.plot(model, score, color=color)
ax2.tick_params(axis='y', labelcolor=color)


fig.tight_layout()  # otherwise the right y-label is slightly clipped



plt.show()






