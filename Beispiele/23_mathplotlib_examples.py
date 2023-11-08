import matplotlib.pyplot as plt

# 1. Draw a line with suitable lable in the x axis
x = range(1,50)
y = [value * 3 for value in x]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
plt.show()                  # Display the figure

# 2. Draw line charts of financial data
import pandas as pd
df = pd.read_csv('.././Daten/mpl_data.csv', sep = ',', parse_dates = True, index_col=0)
df.plot()
plt.xlabel('Date')
plt.ylabel('Euro')
plt.title('Financial Data')
plt.show()

# 3. more then two lines
# line 1 points
x1 = [10, 20, 30]
y1 = [20, 40, 60]
plt.plot(x1, y1, label = 'Line 1')
x2 = [30, 60, 90]
y2 = [40, 10, 30]
plt.plot(x2, y2, label = 'Line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('2 or more lines on the same plot')
plt.show()

# 4. two or more lines with legends, different widths and colors
x1 = [10, 20, 30]
y1 = [20, 40, 60]
x2 = [30, 60, 90]
y2 = [40, 10, 30]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('2 or more lines on the same plot with suitable legends, \ndifferent widths and colors')
plt.plot(x1, y1, color = 'blue', linewidth = 2, label = 'Line 1')
plt.plot(x2, y2, color = 'red', linewidth = 7, label = 'Line 2')
plt.show()

# 5. different line markers
x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

plt.plot(x, y, color = 'red', linestyle = 'dashdot', linewidth = 3, marker = 'o', 
         markerfacecolor = 'blue', markersize = 12)
plt.ylim(1, 8)
plt.xlim(1, 8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Display marker')
plt.show()

# 6. plot several lines with different format stayles in one command using arrays
import numpy as np
t = np.arange(0., 5., 0.2)
# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()

# 7. Create multiple plots
fig = plt.figure()
fig.subplots_adjust(bottom = 0.020, left = 0.020, top = 0.900, right = 0.800)
plt.subplot(2, 1, 1)
plt.xticks(())
plt.yticks(())
plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())
plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())
plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())
plt.show()

##################
# Scatter Plot
#################
from pylab import randn
x = randn(200)
y = randn(200)
plt.scatter(x, y, color = 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# draw a scatter plot with empty circles
# taking a random distribution in x and y
x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x, y, facecolor = 'none', edgecolors = 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Scatter Plot comparing two subjects marks of mathematics and scienc, 10 students
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label = 'Math marks', color = 'r')
plt.xlabel('Marks range')
plt.ylabel('Marks scored')
plt.legend()
plt.show()