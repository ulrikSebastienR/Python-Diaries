'''trying to emulate cheat sheet of datacamp'''

import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color = 'red', linewidth = 3)
