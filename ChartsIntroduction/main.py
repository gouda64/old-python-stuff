import matplotlib.pyplot as plt

classes = ['Little Coders', 'Scratch', 'Intro to Python', 'Python With Pygame']

student = [500, 2000, 400, 600]

plt.title('Students Enrolled in CWK')

plt.xlabel('Class Name')
plt.ylabel('Number of Students Enrolled')
plt.bar(classes, student, color = 'lightblue', label = 'Number of Students')
plt.legend(facecolor = 'lightgreen')

#plt.barh(classes, student, color = 'blue', label = "Number of Students Enrolled")

#plt.plot(classes, student)

plt.show()