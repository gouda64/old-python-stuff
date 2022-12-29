import numpy as np
import matplotlib.pyplot as plt

states = ['NY', 'CA', 'VA', 'TX', 'OH', 'MD', 'DC']
positive = [412, 400, 78, 346, 76, 79, 11]

plt.title('Coronavirus Cases in Various States')

plt.xlabel('States')
plt.ylabel('Coronavirus Cases by Thousands')
plt.legend(facecolor = 'lightgreen')

plt.bar(states, positive, color = 'lightblue', label = 'Cases by the Thousand')

#plt.barh(states, positive, color = 'lightblue', label = 'Cases by the Thousand')

#plt.plot(states, positive)

#plt.pie(positive)

plt.show()