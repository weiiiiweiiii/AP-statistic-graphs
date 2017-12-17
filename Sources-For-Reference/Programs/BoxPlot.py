import numpy as np 
import matplotlib.pyplot as plt 
import mpld3

# Create fake data
# random.normal(mean,sacle(standard deviation),sample size)
# data is pulled from normal datasets so that median and mean are same everytime
# That's the reason why in the figure, line of the median and mean are overlap each other
data1 = np.random.normal(40, 20, 100)
data2 = np.random.normal(50, 30, 100)
data3 = np.random.normal(60, 40, 100)
data4 = np.random.normal(70, 50, 100)

# put all fake datasets into a list    
DataPlot = [data1, data2, data3, data4]

# construct the figure
fig = plt.figure(1, figsize=(9, 6))

# construct an axes 
# like fig.add_subplot(349) means that 
# divide the background of figure into 3 row, 4 column
# and draw the figure on the 9th place from left to right,from top to bottom
# so fig.add_subplot(111) draws the figure right in the middle
axes = fig.add_subplot(111)

# construct the boxplot
BP = axes.boxplot(DataPlot)

# To save the picture
fig.savefig('Box_Plot.png', bbox_inches='tight')

# add patch_artist=True option to axes.boxplot() to get fill color
BP = axes.boxplot(DataPlot, patch_artist=True)

# change outline color, fill color and linewidth of the boxes
for box in BP['boxes']:
    # outline color '#191970' = MidNightBlue
    box.set( color='#191970', linewidth=2)
    # fill color '#FFFF00' = Yellow
    box.set( facecolor = '#FFFF00' )

# change color and linewidth of the medians '#000000' = Black
for median in BP['medians']:
    median.set(color='#000000', linewidth=2)

# put into x-axis labels
axes.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])


print(mpld3.fig_to_html(fig))
