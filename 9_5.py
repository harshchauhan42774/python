import matplotlib.pyplot as plt
import random

# Generating marks for 100 students
student_marks = [random.randint(0, 8) for _ in range(10)]

# Creating a histogram
plt.hist(student_marks, bins=range(0, 9), edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Histogram of Students\' Marks')
plt.xticks(range(0, 5))  # Setting x-axis ticks from 0 to 10
plt.grid(axis='y')  # Adding gridlines along the y-axis
plt.show()