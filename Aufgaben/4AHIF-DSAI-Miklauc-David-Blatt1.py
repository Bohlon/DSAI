import numpy as np
import matplotlib.pyplot as plt

# Generiere fiktive Altersdaten
alter = np.random.normal(loc=35, scale=10, size=500)

# Plot Histogramm
plt.hist(alter, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Alter')
plt.ylabel('Häufigkeit')
plt.title('Histogramm der Altersverteilung')
plt.show()

# Generiere fiktive Daten
stunden_sport = np.random.uniform(low=1, high=10, size=100)
fitness_score = 50 + 3 * stunden_sport + np.random.normal(loc=0, scale=5, size=100)

# Plot Scatterplot
plt.scatter(stunden_sport, fitness_score, color='coral', alpha=0.7)
plt.xlabel('Stunden Sport pro Woche')
plt.ylabel('Fitness-Score')
plt.title('Scatterplot: Stunden Sport vs. Fitness-Score')
plt.show()