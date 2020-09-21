# July 2020
# OBJECCTIVE: CREATE NICE PLOTS: CHECK https://matplotlib.org/gallery.html TO FIND THE NICE PLOTS
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE A FIGURE

my_first_figure = plt.figure("My First Figure")
# subplot
x = np.linspace(0,10,40)
sinx=np.sin(x)
cosx=np.cos(x)
subplot_1 = my_first_figure.add_subplot(2, 3, 1) # 2: Number of rows in the figure, 3: number of column, 1: subplot
plt.plot(sinx)
# Add a plot to specific position in the figure
subplot_6 = my_first_figure.add_subplot(2, 3, 6)
plt.plot(cosx)
#plt.show()

# 2. PLOT MULTIPLE LINES
plt.plot(x,sinx,x,cosx)
#plt.show()


# 3. PLOT IN ONE SIDE BY SIDE GRAPH
plt.subplot(2,1,1)
plt.plot(x,sinx)
plt.title('Two Graph')
plt.ylabel('Sin')

plt.subplot(2,1,2)
plt.plot(x,cosx,'ro')
plt.xlabel('x Value')
plt.ylabel('Cos')


# 4. CREATE HOSTOGRAMS
mu, sigma = 100, 15
data_set = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(data_set, 50, density=1, facecolor='g', alpha=0.75) # 50 bins with normalized value, green color and alphas is transparency
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# 5. PIE CHART
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs'). Means the piece is seperated from the chart

plt.pie(x=sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()

# 6. BAR CHART
N = 5
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)
# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
plt.show()



