from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,87,79,9,85,82,199,67,73,77,9]
# Einteilung in 10er-Schritte, 100 zu den 90ern stecken

histogram = Counter(min(grade // 10*10,90)for grade in grades)
plt.bar([x+5 for x in histogram.keys()],    # verschiebe jeden balken um 5 nach links
    histogram.values(),                     # gib jedem Balken die korrekte Höhe
    10,                                     # gib jedem Balken eine Breite von 10
    edgecolor=(0,0,0))                      # schwarze Ränder für jeden Balken
plt.axis([-5,105,0,5])                      # die x-Achse reicht von -5 bis 105
                                            # die y-Achse reicht von 0 bis 5
plt.xticks([10 * i for i in range(11)])     
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grade")
plt.show()