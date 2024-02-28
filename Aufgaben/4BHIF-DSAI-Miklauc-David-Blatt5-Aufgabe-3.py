import numpy as np
import matplotlib.pyplot as plt

# Vektoren definieren
v1 = np.array([2, 3])
v2 = np.array([4, -1])

# Vektoraddition
v_add = v1 + v2

# Vektorsubtraktion
v_sub = v1 - v2

# Skalarprodukt
dot_prod = np.dot(v1, v2)

# Abstand zweier Vektoren
dist = np.linalg.norm(v1 - v2)

# Plot initialisieren
fig, ax = plt.subplots()

# Ursprung hinzufügen
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Vektoren zeichnen
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
ax.quiver(0, 0, v_add[0], v_add[1], angles='xy', scale_units='xy', scale=1, color='g', label='v1+v2')
ax.quiver(v2[0], v2[1], v1[0]-v2[0], v1[1]-v2[1], angles='xy', scale_units='xy', scale=1, color='m', label='v1-v2')

# Skalarprodukt zeichnen
ax.text(0.5*(v1[0]+v2[0]), 0.5*(v1[1]+v2[1]), str(dot_prod), fontsize=12, color='k')

# Abstand zeichnen
ax.annotate("", xy=v1, xytext=v2, arrowprops=dict(arrowstyle='|-|', color='k'))
ax.text(0.5*(v1[0]+v2[0]), 0.5*(v1[1]+v2[1])+0.5, str(round(dist,2)), fontsize=12, color='k')

# Achsenlimits setzen
ax.set_xlim([-5, 7])
ax.set_ylim([-5, 7])

# Legende hinzufügen
ax.legend()

# Plot anzeigen
plt.show()