import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 28, 25)
menStd = (5, 3, 4, 3, 2)
womenStd = (1, 5, 2, 2, 4)
ind = np.arange(N)   # the x locations for the groups
width = 0.25       # the width of the bars; can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr = menStd, color = "lightblue")
p2 = plt.bar(ind, womenMeans, width, bottom = menMeans, yerr = womenMeans)

plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(8, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()